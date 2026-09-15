"""
Application entry point for the Basic Rule-Based Chatbot.
"""

from chatbot import Chatbot


def main():
    """
    Create and launch the chatbot application.
    """

    chatbot = Chatbot()
    chatbot.start()


if __name__ == "__main__":
    main()