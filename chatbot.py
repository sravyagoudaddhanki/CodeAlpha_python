import time

def bot_reply(message):
    time.sleep(0.5)
    print(f"\n🤖 Bot: {message}\n")

def get_response(user_input):
    msg = user_input.lower()

    if any(word in msg for word in ["hello", "hi", "hey"]):
        return "Hello! 👋 How are you?"

    elif any(word in msg for word in ["how are you", "how r you"]):
        return "I'm doing great! How about you? 😊"

    elif any(word in msg for word in ["good", "fine", "great"]):
        return "That's wonderful! 🌟"

    elif any(word in msg for word in ["sad", "bad", "not good"]):
        return "I'm sorry to hear that! You've got this! 💪"

    elif any(word in msg for word in ["your name", "who are you"]):
        return "I'm AlphaBot 🤖 Nice to meet you!"

    elif any(word in msg for word in ["joke", "funny"]):
        return "Why do programmers hate nature? Too many bugs! 😂"

    elif any(word in msg for word in ["python", "code"]):
        return "Python is amazing! Great choice! 🐍"

    elif any(word in msg for word in ["thank", "thanks"]):
        return "You're welcome! 😊"

    elif any(word in msg for word in ["help"]):
        return "Try saying: hello, joke, how are you, bye!"

    elif any(word in msg for word in ["bye", "goodbye"]):
        return "GOODBYE"

    else:
        return "I don't understand! Try saying hello or help! 😊"

def start_chatbot():
    print("=" * 40)
    print("   🤖 Welcome to AlphaBot!")
    print("=" * 40)
    print("Type a message and press Enter!")
    print("Type 'bye' to exit!\n")

    while True:
        user_input = input("👤 You: ").strip()

        if not user_input:
            print("⚠️ Please type something!\n")
            continue

        response = get_response(user_input)

        if response == "GOODBYE":
            bot_reply("Goodbye! 👋 Have a great day!")
            break

        bot_reply(response)

start_chatbot()