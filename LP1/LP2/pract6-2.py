# Expert System for Hospitals and Medical Facilities

while True:

    print("\n--- Hospital Expert System ---")
    print("1. Cold")
    print("2. Fever")
    print("3. Stomach Pain")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Cold Information
    if choice == 1:
        print("\n--- Cold Related Information ---")
        print("Symptoms:")
        print("- Sneezing")
        print("- Runny nose")
        print("- Cough")

        print("\nTreatment:")
        print("- Drink warm water")
        print("- Take rest")

        print("\nExpert Advice:")
        print("Consult doctor if cold continues.")

    # Fever Information
    elif choice == 2:
        print("\n--- Fever Related Information ---")
        print("Symptoms:")
        print("- High temperature")
        print("- Body pain")
        print("- Weakness")

        print("\nTreatment:")
        print("- Drink more water")
        print("- Take proper rest")

        print("\nExpert Advice:")
        print("Visit doctor if fever becomes high.")

    # Stomach Pain Information
    elif choice == 3:
        print("\n--- Stomach Pain Related Information ---")
        print("Symptoms:")
        print("- Stomach cramps")
        print("- Nausea")
        print("- Bloating")

        print("\nTreatment:")
        print("- Drink warm water")
        print("- Eat light food")
        print("- Take rest")

        print("\nExpert Advice:")
        print("Consult doctor if pain continues.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")