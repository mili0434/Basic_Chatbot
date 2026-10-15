# Task 4: Basic Chatbot
# Description: A simple rule-based chatbot using Python.

def chatbot():
    print("=" * 40)
    print("       WELCOME TO MY CHATBOT")
    print("=" * 40)
    print("Chatbot: Hello! How can I help you?")
    print("Chatbot: Type 'hello', 'how are you', or 'bye' to chat.")
    print("-" * 40)

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Chatbot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How about you?")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input == "help":
            print("Chatbot: You can type 'hello', 'how are you', or 'bye'.")

        else:
            print("Chatbot: Sorry, I don't understand that. Please try again.")

        print()

    print("Chatbot session ended.")


# Run the chatbot
if __name__ == "__main__":
    chatbot()