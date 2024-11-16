from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Securely load the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    if not user_message:
        return jsonify({"response": "Please provide a message."}), 400

    try:
        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_message,
            max_tokens=100
        )
        bot_response = response.choices[0].text.strip()
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
