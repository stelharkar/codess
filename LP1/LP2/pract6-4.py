# Expert System for Employee Performance Evaluation

while True:

    print("\n--- Employee Performance Evaluation System ---")
    print("1. Excellent Performance")
    print("2. Average Performance")
    print("3. Poor Performance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Excellent Performance
    if choice == 1:
        print("\n--- Excellent Performance ---")
        print("Details:")
        print("- Work completed on time")
        print("- High productivity")
        print("- Good teamwork")

        print("\nExpert Advice:")
        print("Employee deserves promotion or rewards.")

    # Average Performance
    elif choice == 2:
        print("\n--- Average Performance ---")
        print("Details:")
        print("- Work completed with delay")
        print("- Normal productivity")

        print("\nExpert Advice:")
        print("Employee needs motivation and training.")

    # Poor Performance
    elif choice == 3:
        print("\n--- Poor Performance ---")
        print("Details:")
        print("- Incomplete tasks")
        print("- Low productivity")

        print("\nExpert Advice:")
        print("Employee needs improvement and guidance.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")