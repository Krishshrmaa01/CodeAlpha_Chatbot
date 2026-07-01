def chatbot():
    print("🤖 Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user = input("You: ").lower()
        if user == "bye":
            print("🤖 Goodbye! 👋")
            break
        elif user in ["hello", "hi"]:
            print("🤖 Hello! How can I help?")
        elif user in ["how are you", "how r u"]:
            print("🤖 I'm fine, thanks! 😊")
        elif "name" in user:
            print("🤖 I'm CodeAlpha Bot!")
        else:
            print("🤖 I don't understand that yet.")

chatbot()