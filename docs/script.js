"use strict";

const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const messages = document.getElementById("chatMessages");
const send = document.getElementById("sendButton");
const typing = document.getElementById("typingIndicator");
const clear = document.getElementById("clearChat");

function time() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

function clean(text) {
    return text.trim().toLowerCase().replace(/\s+/g, " ");
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function response(text) {
    const msg = clean(text);

    if (!msg) return "Please enter a message. ??";

    if (["hello", "hi", "hey", "hello bot", "hi bot"].includes(msg))
        return "Hello! ?? How can I help you today?";

    if (["how are you", "how are you doing", "how are you today"].includes(msg))
        return "I'm doing great, thanks for asking! ??";

    if (["thanks", "thank you", "thanks a lot"].includes(msg))
        return "You're welcome! ??";

    if (msg === "time")
        return `The current time is ${time()}. ??`;

    if (msg === "date")
        return `Today's date is ${new Date().toLocaleDateString("en-GB", {
            day: "2-digit",
            month: "long",
            year: "numeric"
        })}. ??`;

    if (["help", "commands", "menu"].includes(msg))
        return "Available commands: hello, how are you, thanks, time, date, help, bye.";

    if (["bye", "goodbye", "good bye", "exit", "quit"].includes(msg))
        return "Goodbye! ?? Have a great day!";

    return "I'm still learning. Try asking something else. ??";
}

function addMessage(text, sender) {
    const item = document.createElement("div");
    item.className = `message ${sender}-message`;

    item.innerHTML = `
        <div class="message-avatar">${sender === "bot" ? "??" : "??"}</div>
        <div class="message-content">
            <div class="message-bubble">${escapeHtml(text)}</div>
            <span class="message-time">${time()}</span>
        </div>
    `;

    messages.appendChild(item);
    messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const text = input.value.trim();
    if (!text) return;

    addMessage(text, "user");
    input.value = "";

    typing.classList.remove("hidden");
    send.disabled = true;

    await new Promise(resolve => setTimeout(resolve, 450));

    typing.classList.add("hidden");
    addMessage(response(text), "bot");

    send.disabled = false;
    input.focus();
});

clear.addEventListener("click", () => {
    messages.innerHTML = `
        <div class="message bot-message">
            <div class="message-avatar">??</div>
            <div class="message-content">
                <div class="message-bubble">Chat cleared! ?? How can I help you?</div>
                <span class="message-time">${time()}</span>
            </div>
        </div>
    `;
    input.focus();
});

input.focus();
