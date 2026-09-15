"""
Core engine for the Basic Rule-Based Chatbot.

The chatbot uses predefined rules and does not require
an external AI API or internet connection.
"""

import random

from .responses import (
    GREETINGS,
    HOW_ARE_YOU,
    THANKS,
    GOODBYES,
    HELP_COMMANDS,
    RESPONSES,
    HELP_MESSAGE,
)

from .utils import (
    clean_input,
    get_current_time,
    get_current_date,
)


class Chatbot:
    """
    Main chatbot class.

    Handles user input, applies predefined rules,
    and generates appropriate responses.
    """

    def __init__(self):
        """Initialize the chatbot."""

        self.running = True
        self.message_count = 0

    def get_response(self, user_input: str) -> str:
        """
        Generate a chatbot response.

        Args:
            user_input: Message entered by the user.

        Returns:
            Appropriate chatbot response.
        """

        message = clean_input(user_input)

        # Count every user message.
        self.message_count += 1

        # -------------------------------------------------
        # Empty Input
        # -------------------------------------------------

        if not message:
            return "Please enter a message. 😊"

        # -------------------------------------------------
        # Greeting
        # -------------------------------------------------

        elif message in GREETINGS:
            return random.choice(RESPONSES["greeting"])

        # -------------------------------------------------
        # How Are You
        # -------------------------------------------------

        elif message in HOW_ARE_YOU:
            return random.choice(RESPONSES["how_are_you"])

        # -------------------------------------------------
        # Thank You
        # -------------------------------------------------

        elif message in THANKS:
            return random.choice(RESPONSES["thanks"])

        # -------------------------------------------------
        # Current Time
        # -------------------------------------------------

        elif message == "time":
            current_time = get_current_time()
            return f"The current time is {current_time}. 🕐"

        # -------------------------------------------------
        # Current Date
        # -------------------------------------------------

        elif message == "date":
            current_date = get_current_date()
            return f"Today's date is {current_date}. 📅"

        # -------------------------------------------------
        # Help
        # -------------------------------------------------

        elif message in HELP_COMMANDS:
            return HELP_MESSAGE

        # -------------------------------------------------
        # Goodbye
        # -------------------------------------------------

        elif message in GOODBYES:
            self.running = False
            return random.choice(RESPONSES["goodbye"])

        # -------------------------------------------------
        # Unknown Input
        # -------------------------------------------------

        else:
            return random.choice(RESPONSES["unknown"])

    def start(self):
        """
        Start the chatbot conversation.

        The while loop keeps the chatbot active until
        the user enters a goodbye command.
        """

        self._display_welcome()

        while self.running:

            try:
                user_input = input("\nYou: ")

                response = self.get_response(user_input)

                print(f"Bot: {response}")

            except KeyboardInterrupt:
                print("\n\nBot: Goodbye! 👋")
                self.running = False

            except EOFError:
                print("\nBot: Goodbye! 👋")
                self.running = False

    @staticmethod
    def _display_welcome():
        """Display the chatbot welcome screen."""

        print()
        print("=" * 60)
        print("🤖  BASIC RULE-BASED CHATBOT")
        print("=" * 60)
        print("Hello! I'm your Python chatbot.")
        print("Type 'help' to see available commands.")
        print("Type 'bye' or 'exit' to end the conversation.")
        print("=" * 60)