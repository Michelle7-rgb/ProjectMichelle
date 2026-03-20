const main = document.getElementById("mainContent");
const themeToggle = document.getElementById("themeToggle");
const collapseBtn = document.getElementById("collapseBtn");
const mobileMenuBtn = document.getElementById("mobileMenuBtn");
const sidebarBackdrop = document.getElementById("sidebarBackdrop");
const sidebar = document.getElementById("sidebar");
const navLinks = document.querySelectorAll("nav a[data-spa='true']");

function isMobile() {
    return window.matchMedia("(max-width: 900px)").matches;
}

function setMobileMenuState(isOpen) {
    if (!sidebar || !mobileMenuBtn) {
        return;
    }

    document.body.classList.toggle("sidebar-open", isOpen);
    sidebar.classList.toggle("mobile-open", isOpen);
    mobileMenuBtn.textContent = isOpen ? "✕" : "☰";
    mobileMenuBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
}

if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
}

if (themeToggle) {
    themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
    themeToggle.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        localStorage.setItem(
            "theme",
            document.body.classList.contains("dark") ? "dark" : "light"
        );
        themeToggle.textContent = document.body.classList.contains("dark") ? "☀️" : "🌙";
    });
}

if (collapseBtn && sidebar) {
    collapseBtn.addEventListener("click", () => {
        if (isMobile()) {
            setMobileMenuState(!sidebar.classList.contains("mobile-open"));
        }
    });
}

if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener("click", () => {
        if (!sidebar) {
            return;
        }

        setMobileMenuState(!sidebar.classList.contains("mobile-open"));
    });
}

if (sidebarBackdrop) {
    sidebarBackdrop.addEventListener("click", () => {
        setMobileMenuState(false);
    });
}

function setActiveLink(pathname) {
    navLinks.forEach((link) => {
        const linkPath = new URL(link.href, window.location.origin).pathname;
        link.classList.toggle("active", linkPath === pathname);
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

        if (push) {
            window.history.pushState({}, "", url);
        }
    } catch {
        window.location.href = url;
    }
}

navLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
        event.preventDefault();
        loadPage(link.href, true);
        if (isMobile()) {
            setMobileMenuState(false);
        }
    });
});

window.addEventListener("popstate", () => {
    loadPage(window.location.href, false);
});

window.addEventListener("resize", () => {
    if (!isMobile()) {
        setMobileMenuState(false);
    }
});

document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && isMobile()) {
        setMobileMenuState(false);
    }
});

setActiveLink(window.location.pathname);

function sendMessage() {
    const input = document.getElementById("msgInput");
    const chat = document.getElementById("chatMessages");

    if (!input || !chat) {
        return;
    }

    if (input.value.trim() !== "") {
        const msg = document.createElement("div");
        msg.classList.add("message", "sent");
        msg.innerText = input.value;
        chat.appendChild(msg);
        input.value = "";
        chat.scrollTop = chat.scrollHeight;
    }
}

document.addEventListener("submit", (event) => {
    if (event.target && event.target.id === "chatForm") {
        event.preventDefault();
        sendMessage();
    }
});