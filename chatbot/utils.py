"""
Utility functions for the Basic Rule-Based Chatbot.
"""

from datetime import datetime


def clean_input(user_input: str) -> str:
    """
    Normalize user input.

    Removes unnecessary spaces and converts the input
    to lowercase for easier command matching.

    Args:
        user_input: Raw text entered by the user.

    Returns:
        Cleaned and normalized user input.
    """

    return " ".join(user_input.strip().lower().split())


def get_current_time() -> str:
    """
    Get the current system time.

    Returns:
        Current time formatted as HH:MM:SS AM/PM.
    """

    return datetime.now().strftime("%I:%M:%S %p")


def get_current_date() -> str:
    """
    Get the current system date.

    Returns:
        Current date formatted as DD Month YYYY.
    """

    return datetime.now().strftime("%d %B %Y")