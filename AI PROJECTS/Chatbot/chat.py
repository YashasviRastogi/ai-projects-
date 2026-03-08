print("🤖 INTELLIGENT CUSTOMER SUPPORT CHATBOT")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ").lower()
    
    if "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I help you today?")
    elif "refund" in user_input:
        print("Chatbot: Please provide your order ID for refund processing.")
    elif "price" in user_input:
        print("Chatbot: Our premium plan is $9.99/month. Enter 'plans' for details.")
    elif "quit" in user_input:
        print("Chatbot: Thank you for chatting! Goodbye! 👋")
        break
    else:
        print("Chatbot: Sorry, I didn't understand. Try 'refund', 'price', or 'hello'.")
