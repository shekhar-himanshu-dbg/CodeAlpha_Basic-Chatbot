"use strict";

const form = document.getElementById("chatForm");
const input = document.getElementById("messageInput");
const messages = document.getElementById("chatMessages");
const clearButton = document.getElementById("clearChat");

function cleanInput(text) {
    return text.trim().toLowerCase().replace(/\s+/g, " ");
}

function getTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

function getResponse(message) {
    const text = cleanInput(message);

    if (!text) {
        return "Please enter a message. 😊";
    }

    if (["hello", "hi", "hey", "hello bot", "hi bot"].includes(text)) {
        return "Hello! 👋 How can I help you today?";
    }

    if (["how are you", "how are you doing", "how are you today"].includes(text)) {
        return "I'm doing great, thanks for asking! 😊";
    }

    if (["thanks", "thank you", "thanks a lot"].includes(text)) {
        return "You're welcome! 😊";
    }

    if (text === "time") {
        return `The current time is ${getTime()}. 🕐`;
    }

    if (text === "date") {
        return `Today's date is ${new Date().toLocaleDateString("en-GB", {
            day: "2-digit",
            month: "long",
            year: "numeric"
        })}. 📅`;
    }

    if (["help", "commands", "menu"].includes(text)) {
        return "Available commands: hello, how are you, thanks, time, date, help, bye.";
    }

    if (["bye", "goodbye", "good bye", "exit", "quit"].includes(text)) {
        return "Goodbye! 👋 Have a great day!";
    }

    return "I'm still learning. Try asking something else. 🤖";
}

function escapeHTML(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function addMessage(text, sender) {
    const welcome = document.getElementById("welcome");

    if (welcome) {
        welcome.remove();
    }

    const message = document.createElement("div");
    message.className = `message ${sender}-message`;

    message.innerHTML = `
        <div>
            <div class="bubble">${escapeHTML(text)}</div>
            <div class="time">${getTime()}</div>
        </div>
    `;

    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const text = input.value.trim();

    if (!text) {
        return;
    }

    addMessage(text, "user");

    input.value = "";

    setTimeout(() => {
        addMessage(getResponse(text), "bot");
    }, 400);
});

clearButton.addEventListener("click", () => {
    messages.innerHTML = `
        <div class="welcome" id="welcome">
            <h2>Welcome! 👋</h2>
            <p>I'm a simple rule-based chatbot.</p>
            <br>
            <p>Try: <b>hello</b>, <b>how are you</b>, <b>time</b>, <b>date</b>, <b>help</b></p>
        </div>
    `;

    input.focus();
});

input.focus();