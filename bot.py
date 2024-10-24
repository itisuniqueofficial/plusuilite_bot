from flask import Flask, request, jsonify
import requests

# Telegram Bot Token (replace with your bot token)
BOT_TOKEN = "api.js"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/send-message", methods=["POST"])
def send_message():
    try:
        data = request.json  # Get JSON data from the POST request
        name = data.get("name")
        phone = data.get("phone")
        username = data.get("username")
        message_content = data.get("message")

        # Validate inputs
        if not (name and phone and username and message_content):
            return jsonify({"status": "error", "message": "Invalid input"}), 400

        if not username.startswith("@"):
            return jsonify({"status": "error", "message": "Username must start with '@'."}), 400

        # Format the message
        message = (
            f"📇 *New Contact Message*\n\n"
            f"👤 Name: {name}\n"
            f"📱 Phone: {phone}\n"
            f"💬 Message: {message_content}\n\n"
            f"Contacting: {username}"
        )

        # Send the message to the provided Telegram username
        response = requests.post(TELEGRAM_API_URL, json={
            "chat_id": username,
            "text": message,
            "parse_mode": "Markdown"
        })

        # Check for Telegram API response
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Message sent successfully!"}), 200
        else:
            return jsonify({"status": "error", "message": response.text}), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
