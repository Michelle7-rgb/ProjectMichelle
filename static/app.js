const main = document.getElementById("mainContent");
const themeToggle = document.getElementById("themeToggle");
const mobileMenuBtn = document.getElementById("mobileMenuBtn");
const mobileMenuPanel = document.getElementById("mobileMenuPanel");

function safeStorageGet(key) {
    try {
        return localStorage.getItem(key);
    } catch {
        return null;
    }
}

function safeStorageSet(key, value) {
    try {
        localStorage.setItem(key, value);
    } catch {
        // Ignore storage errors (private mode / blocked storage).
    }
}

function getSpaLinks() {
    return document.querySelectorAll("a[data-spa='true']");
}

function setMobileMenuState(isOpen) {
    if (!mobileMenuBtn || !mobileMenuPanel) {
        return;
    }

    document.body.classList.toggle("mobile-menu-open", isOpen);
    mobileMenuBtn.textContent = isOpen ? "✕" : "☰";
    mobileMenuBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    mobileMenuPanel.setAttribute("aria-hidden", isOpen ? "false" : "true");
}

function bindSpaLinks() {
    const links = getSpaLinks();
    links.forEach((link) => {
        link.addEventListener("click", (event) => {
            event.preventDefault();
            loadPage(link.href, true);
            setMobileMenuState(false);
        });
    });
}

function setActiveLink(pathname) {
    getSpaLinks().forEach((link) => {
        try {
            const linkPath = new URL(link.href, window.location.origin).pathname;
            link.classList.toggle("active", linkPath === pathname);
        } catch {
            link.classList.remove("active");
        }
    });
}

if (safeStorageGet("theme") === "dark") {
    document.body.classList.add("dark");
}

if (themeToggle) {
    themeToggle.textContent = document.body.classList.contains("dark") ? "☀" : "◐";
    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        safeStorageSet("theme", document.body.classList.contains("dark") ? "dark" : "light");
        themeToggle.textContent = document.body.classList.contains("dark") ? "☀" : "◐";
    });
}

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener("click", () => {
        setMobileMenuState(!document.body.classList.contains("mobile-menu-open"));
    });
}

if (mobileMenuPanel) {
    mobileMenuPanel.addEventListener("click", (event) => {
        if (event.target instanceof HTMLAnchorElement) {
            setMobileMenuState(false);
        }
    });
}

async function loadPage(url, push = true) {
    if (!main) {
        window.location.href = url;
        return;
    }

    try {
        const response = await fetch(url, {
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        });

        if (!response.ok) {
            window.location.href = url;
            return;
        }

        const html = await response.text();
        const doc = new DOMParser().parseFromString(html, "text/html");
        const incomingMain = doc.getElementById("mainContent");

        if (!incomingMain) {
            window.location.href = url;
            return;
        }

        main.innerHTML = incomingMain.innerHTML;
        const pathname = new URL(url, window.location.origin).pathname;
        setActiveLink(pathname);
        bindSpaLinks();

        if (push) {
            window.history.pushState({}, "", url);
        }
    } catch {
        window.location.href = url;
    }
}

window.addEventListener("popstate", () => {
    loadPage(window.location.href, false);
});

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        setMobileMenuState(false);
    }
});

bindSpaLinks();
setActiveLink(window.location.pathname);
