def chatbot():
    print("Chatbot: Hi! Type something to begin. Type 'bye' to end.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hello there!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "hi":
            print("Chatbot: Hi!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
