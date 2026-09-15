"""
Response configuration for the Basic Rule-Based Chatbot.

This module contains predefined user commands and chatbot responses.
Keeping them separate from the chatbot engine makes the application
cleaner and easier to maintain.
"""

# ---------------------------------------------------------
# User Command Groups
# ---------------------------------------------------------

GREETINGS = {
    "hello",
    "hi",
    "hey",
    "hello bot",
    "hi bot",
    "good morning",
    "good afternoon",
    "good evening",
}

HOW_ARE_YOU = {
    "how are you",
    "how are you doing",
    "how are you today",
    "how do you feel",
}

THANKS = {
    "thanks",
    "thank you",
    "thanks a lot",
    "thank you so much",
}

GOODBYES = {
    "bye",
    "goodbye",
    "good bye",
    "see you",
    "see you later",
    "exit",
    "quit",
}

HELP_COMMANDS = {
    "help",
    "commands",
    "menu",
}


# ---------------------------------------------------------
# Chatbot Responses
# ---------------------------------------------------------

RESPONSES = {
    "greeting": [
        "Hello! 👋",
        "Hi there! 😊",
        "Hey! Nice to meet you.",
        "Hello! How can I help you today?",
    ],

    "how_are_you": [
        "I'm doing great, thanks for asking! 😊",
        "I'm fine, thank you!",
        "I'm working perfectly! 🤖",
        "I'm doing well. How about you?",
    ],

    "thanks": [
        "You're welcome! 😊",
        "My pleasure!",
        "Anytime! 👍",
        "Happy to help!",
    ],

    "goodbye": [
        "Goodbye! 👋 Have a great day!",
        "See you soon! 😊",
        "Take care! Goodbye!",
        "It was nice chatting with you!",
    ],

    "unknown": [
        "I'm sorry, I don't understand that yet.",
        "Could you please rephrase that?",
        "I'm still learning. Try asking something else.",
        "I don't have a response for that yet. 🤖",
    ],
}


# ---------------------------------------------------------
# Help Message
# ---------------------------------------------------------

HELP_MESSAGE = """
╔══════════════════════════════════════════════════════╗
║                  🤖 CHATBOT HELP                    ║
╠══════════════════════════════════════════════════════╣
║ hello / hi       → Greeting                         ║
║ how are you      → Ask about the chatbot            ║
║ thanks           → Thank the chatbot                ║
║ time             → Show current time                ║
║ date             → Show current date                ║
║ help             → Show this help menu              ║
║ bye / exit       → End the conversation             ║
╚══════════════════════════════════════════════════════╝
"""