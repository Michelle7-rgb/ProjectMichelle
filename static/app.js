const themeToggle = document.getElementById("themeToggle");
const collapseBtn = document.getElementById("collapseBtn");
const sidebar = document.getElementById("sidebar");

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
        sidebar.classList.toggle("collapsed");
    });
}

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
