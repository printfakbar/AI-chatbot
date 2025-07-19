import json
from datetime import datetime
try:
    with open("C:/Users/akbar/Videos/Captures/tasks/ChatBot/response.json", "r") as file:
        responses = json.load(file)
except FileNotFoundError:
    print(" Error: response.json not found.")
    exit()

log_file =  "C:/Users/akbar/Videos/Captures/tasks/ChatBot/ChatHistory.txt"

def log_to_file(user_input, bot_response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"Chatbot: {bot_response}\n")

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        return responses.get("hi", "Hello!")

    elif user_input in ["bye", "exit", "quit", "goodbye"]:
        return responses.get("bye", "Goodbye!")

    elif "time" in user_input:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

    elif "date" in user_input:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}"

    elif user_input in ["how are you", "how are you doing"]:
        return responses.get("how_are_you", "I'm good!")

    elif user_input in ["what can you do", "help", "features"]:
        return responses.get("abilities", "I can chat and show time/date!")

    elif user_input in ["who created you", "who made you"]:
        return responses.get("creator", "I was created for an AI project.")

    elif user_input in ["thank you", "thanks"]:
        return responses.get("thanks", "You're welcome!")

    elif user_input in ["are you a robot", "are you human"]:
        return responses.get("robot", "I'm a chatbot ")

    elif user_input in ["tell me a joke", "joke"]:
        return responses.get("joke", "Why did the AI fail school? Too many logic errors!")

    else:
        return "Sorry, I didn't understand that."
while True:
    user_msg = input("You: ")
    bot_msg = get_response(user_msg)

    print("Chatbot:", bot_msg)
    log_to_file(user_msg, bot_msg)

    if user_msg.lower().strip() in ["bye", "exit", "quit", "goodbye"]:
        break
