# Expert System for Information Management

while True:

    print("\n--- Information Management Expert System ---")
    print("1. Student Information")
    print("2. Employee Information")
    print("3. Library Information")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Student Information
    if choice == 1:
        print("\n--- Student Information ---")
        print("Details:")
        print("- Name: Rahul")
        print("- Course: Computer Engineering")
        print("- Year: Third Year")

        print("\nManagement Advice:")
        print("Maintain attendance and study regularly.")

    # Employee Information
    elif choice == 2:
        print("\n--- Employee Information ---")
        print("Details:")
        print("- Name: Amit")
        print("- Department: HR")
        print("- Salary: 30000")

        print("\nManagement Advice:")
        print("Update employee records regularly.")

    # Library Information
    elif choice == 3:
        print("\n--- Library Information ---")
        print("Details:")
        print("- Book Name: Python Programming")
        print("- Author: ABC")
        print("- Available Copies: 10")

        print("\nManagement Advice:")
        print("Return books on time.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")