""" Develop an elementary chatbot for any suitable customer interaction application."""

# Elementary Chatbot for Customer Interaction

print("----- Customer Support Chatbot -----")
print("Type 'bye' to exit")

while True:

    user = input("\nYou: ").lower()

    # Greeting
    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    # Product information
    elif "product" in user:
        print("Bot: We have laptops, mobiles, and headphones.")

    # Price inquiry
    elif "price" in user:
        print("Bot: Prices depend on the product selected.")

    # Order status
    elif "order" in user:
        print("Bot: Your order will be delivered in 3 days.")

    # Delivery information
    elif "delivery" in user:
        print("Bot: Delivery is available all over India.")

    # Thank you message
    elif "thank" in user:
        print("Bot: Welcome! Happy to help you.")

    # Exit
    elif user == "bye":
        print("Bot: Thank you for visiting!")
        break

    # Default response
    else:
        print("Bot: Sorry, I did not understand.")