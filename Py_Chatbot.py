responses = {
    "hello": "Hi! How can I help you? 😊",
    "how are you": "I'm doing great! Thanks for asking! 😄",
    "what is python": "Python is a powerful programming language! 🐍",
    "bye": "Goodbye! Have a great day! 👋",
    "your name": "My name is PyBot! 🤖",
    "help": "I can answer basic questions! Try asking me something! 😊",
}

def chatbot(user_input):
    user_input = user_input.lower().strip()
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return "I don't understand that. Can you ask something else? 🤔"

print("╔══════════════════════════════════╗")
print("║       🤖 PYBOT CHATBOT 🤖        ║")
print("╚══════════════════════════════════╝")
print("Type 'bye' to exit!\n")

while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("PyBot: Goodbye! 👋")
        break
    response = chatbot(user_input)
    print(f"PyBot: {response}")