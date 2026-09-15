"use strict";

const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatMessages = document.getElementById("chatMessages");
const sendButton = document.getElementById("sendButton");
const typingIndicator = document.getElementById("typingIndicator");
const clearChatButton = document.getElementById("clearChat");


/**
 * Get current time in a readable format.
 */
function getCurrentTime() {
    return new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}


/**
 * Escape HTML to prevent unwanted markup.
 */
function escapeHtml(text) {
    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


/**
 * Add a message to the chat window.
 */
function addMessage(message, sender) {

    const messageElement = document.createElement("div");

    messageElement.className =
        `message ${sender}-message`;

    const avatar =
        sender === "bot" ? "🤖" : "👤";

    messageElement.innerHTML = `
        <div class="message-avatar">
            ${avatar}
        </div>

        <div class="message-content">

            <div class="message-bubble">
                ${escapeHtml(message)}
            </div>

            <span class="message-time">
                ${getCurrentTime()}
            </span>

        </div>
    `;

    chatMessages.appendChild(messageElement);

    scrollToBottom();
}


/**
 * Scroll chat to the latest message.
 */
function scrollToBottom() {
    chatMessages.scrollTop =
        chatMessages.scrollHeight;
}


/**
 * Show typing animation.
 */
function showTyping() {
    typingIndicator.classList.remove("hidden");

    scrollToBottom();
}


/**
 * Hide typing animation.
 */
function hideTyping() {
    typingIndicator.classList.add("hidden");
}


/**
 * Enable/disable input controls.
 */
function setLoading(loading) {

    sendButton.disabled = loading;
    messageInput.disabled = loading;

    if (!loading) {
        messageInput.focus();
    }
}


/**
 * Send message to Flask backend.
 */
async function sendMessage(message) {

    try {

        showTyping();
        setLoading(true);

        // Small delay for a natural chatbot experience.
        await new Promise(
            resolve => setTimeout(resolve, 500)
        );

        const response = await fetch("/api/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })
        });


        if (!response.ok) {
            throw new Error(
                `Server error: ${response.status}`
            );
        }


        const data = await response.json();

        hideTyping();

        addMessage(
            data.response,
            "bot"
        );


    } catch (error) {

        hideTyping();

        addMessage(
            "Sorry, something went wrong. Please try again.",
            "bot"
        );

        console.error(error);

    } finally {

        setLoading(false);
    }
}


/**
 * Handle form submission.
 */
chatForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();

        const message =
            messageInput.value.trim();

        if (!message) {
            return;
        }

        addMessage(
            message,
            "user"
        );

        messageInput.value = "";

        await sendMessage(message);
    }
);


/**
 * Clear chat history.
 */
clearChatButton.addEventListener(
    "click",
    function () {

        chatMessages.innerHTML = `
            <div class="message bot-message">

                <div class="message-avatar">
                    🤖
                </div>

                <div class="message-content">

                    <div class="message-bubble">
                        Chat cleared! 👋
                        How can I help you?
                    </div>

                    <span class="message-time">
                        ${getCurrentTime()}
                    </span>

                </div>

            </div>
        `;

        messageInput.focus();
    }
);


/**
 * Focus input when page loads.
 */
window.addEventListener(
    "load",
    function () {
        messageInput.focus();
    }
);