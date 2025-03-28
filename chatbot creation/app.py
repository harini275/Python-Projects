
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# A dictionary that maps keywords to predefined responses
responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "welcome": "Thanks, welcome back to the chatbot",
    "default": "I'm not sure I understand. Could you please rephrase it?"
}

# Function to find appropriate response based on the user's input
def chatbot_response(user_input):
    user_input = user_input.lower()
    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
    return responses["default"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json['message']
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)





