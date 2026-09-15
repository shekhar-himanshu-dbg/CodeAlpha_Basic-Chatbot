"""
Flask web application for the Basic Rule-Based Chatbot.
"""

from flask import Flask, jsonify, render_template, request

from chatbot import Chatbot


app = Flask(__name__)

# Create one chatbot instance for the application.
chatbot = Chatbot()


@app.route("/")
def home():
    """Render the chatbot web interface."""

    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """Process a user message and return a chatbot response."""

    data = request.get_json(silent=True) or {}

    user_message = data.get("message", "")

    response = chatbot.get_response(user_message)

    return jsonify({
        "response": response,
        "message_count": chatbot.message_count,
        "running": chatbot.running
    })


@app.route("/api/health")
def health():
    """Return application health status."""

    return jsonify({
        "status": "online",
        "service": "Basic Rule-Based Chatbot"
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )