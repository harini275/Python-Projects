# Import the regular expression module to handle pattern matching
import re

# A dictionary that maps keywords to predefined responses
responses = {
    "commands": "Available commands: hello, hi, how are you, what is your name, help, bye, thank you",

    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I'm a chatbot created to assist you.",
    "help": "Sure, I'm here to help. What do you need assistance with?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! I'm happy to help.",
    "default": "I'm not sure I understand. Could you please rephrase?"
}

# Function to find the appropriate response based on the user's input
def display_commands():
    print(responses["commands"])

def chatbot_response(user_input):
    display_commands()  # Show commands on the first interaction

    # Convert user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()
    
    for keyword in responses:
        if re.search(keyword, user_input):
            return responses[keyword]
    
    return responses["default"]

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hello! I'm here to assist you. (type 'commands' to see available commands, or 'bye' to exit)")

    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # If user types 'bye', exit the loop
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get chatbot's response based on user input
        response = chatbot_response(user_input)
        print("Chatbot:", response)
