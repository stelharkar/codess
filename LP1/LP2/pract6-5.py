# Expert System for Stock Market Trading

while True:

    print("\n--- Stock Market Trading Expert System ---")
    print("1. Buy Stock")
    print("2. Sell Stock")
    print("3. Hold Stock")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Buy Stock
    if choice == 1:
        print("\n--- Buy Stock Advice ---")
        print("Market Condition:")
        print("- Stock prices are increasing")
        print("- Company performance is good")

        print("\nExpert Advice:")
        print("Good time to buy stocks.")

    # Sell Stock
    elif choice == 2:
        print("\n--- Sell Stock Advice ---")
        print("Market Condition:")
        print("- Stock prices are falling")
        print("- Market risk is high")

        print("\nExpert Advice:")
        print("Good time to sell stocks.")

    # Hold Stock
    elif choice == 3:
        print("\n--- Hold Stock Advice ---")
        print("Market Condition:")
        print("- Market is stable")

        print("\nExpert Advice:")
        print("Hold stocks and wait for better opportunity.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")