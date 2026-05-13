# Expert System for Help Desk Management

while True:

    print("\n--- Help Desk Management Expert System ---")
    print("1. Password Reset")
    print("2. Internet Problem")
    print("3. Printer Problem")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Password Reset
    if choice == 1:
        print("\n--- Password Reset Information ---")
        print("Problem:")
        print("- User forgot password")
        print("- Unable to login")

        print("\nSolution:")
        print("- Click on 'Forgot Password'")
        print("- Enter registered email")
        print("- Create new password")

        print("\nExpert Advice:")
        print("Use strong passwords and update regularly.")

    # Internet Problem
    elif choice == 2:
        print("\n--- Internet Problem Information ---")
        print("Problem:")
        print("- Internet not working")
        print("- Slow connection")

        print("\nSolution:")
        print("- Restart router")
        print("- Check network cables")
        print("- Contact ISP if issue continues")

        print("\nExpert Advice:")
        print("Keep network devices updated.")

    # Printer Problem
    elif choice == 3:
        print("\n--- Printer Problem Information ---")
        print("Problem:")
        print("- Printer not printing")
        print("- Paper jam")

        print("\nSolution:")
        print("- Check printer connection")
        print("- Remove jammed paper")
        print("- Restart printer")

        print("\nExpert Advice:")
        print("Maintain printer regularly.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")