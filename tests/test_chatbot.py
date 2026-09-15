"""
Automated tests for the Basic Rule-Based Chatbot.

Run the tests with:

    python -m pytest
"""

from chatbot import Chatbot


def test_greeting():
    """Test that the chatbot responds to a greeting."""

    chatbot = Chatbot()

    response = chatbot.get_response("hello")

    assert response in [
        "Hello! 👋",
        "Hi there! 😊",
        "Hey! Nice to meet you.",
        "Hello! How can I help you today?",
    ]


def test_greeting_case_insensitive():
    """Test that uppercase input is handled correctly."""

    chatbot = Chatbot()

    response = chatbot.get_response("HELLO")

    assert response != ""


def test_how_are_you():
    """Test the how-are-you response."""

    chatbot = Chatbot()

    response = chatbot.get_response("how are you")

    assert response != ""


def test_thanks():
    """Test the thank-you response."""

    chatbot = Chatbot()

    response = chatbot.get_response("thanks")

    assert response != ""


def test_time():
    """Test the time command."""

    chatbot = Chatbot()

    response = chatbot.get_response("time")

    assert "current time" in response.lower()


def test_date():
    """Test the date command."""

    chatbot = Chatbot()

    response = chatbot.get_response("date")

    assert "today's date" in response.lower()


def test_help():
    """Test the help command."""

    chatbot = Chatbot()

    response = chatbot.get_response("help")

    assert "CHATBOT HELP" in response


def test_unknown_message():
    """Test an unknown user message."""

    chatbot = Chatbot()

    response = chatbot.get_response("something completely unknown")

    assert response != ""


def test_empty_input():
    """Test empty user input."""

    chatbot = Chatbot()

    response = chatbot.get_response("")

    assert "Please enter" in response


def test_goodbye():
    """Test the goodbye command."""

    chatbot = Chatbot()

    response = chatbot.get_response("bye")

    assert response != ""
    assert chatbot.running is False