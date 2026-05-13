# Expert System for Airline Scheduling and Cargo Schedules

while True:

    print("\n--- Airline Scheduling Expert System ---")
    print("1. Passenger Flight Schedule")
    print("2. Cargo Flight Schedule")
    print("3. Delayed Flight")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # Passenger Flight
    if choice == 1:
        print("\n--- Passenger Flight Schedule ---")
        print("Flight Number: AI101")
        print("Departure: 10:00 AM")
        print("Arrival: 12:00 PM")

        print("\nExpert Advice:")
        print("Passengers should arrive 2 hours early.")

    # Cargo Flight
    elif choice == 2:
        print("\n--- Cargo Flight Schedule ---")
        print("Cargo Flight Number: CG202")
        print("Departure: 3:00 PM")
        print("Destination: Delhi")

        print("\nExpert Advice:")
        print("Check cargo weight before loading.")

    # Delayed Flight
    elif choice == 3:
        print("\n--- Delayed Flight Information ---")
        print("Reason:")
        print("- Bad weather")
        print("- Technical issue")

        print("\nExpert Advice:")
        print("Passengers should check updated timings.")

    # Exit
    elif choice == 4:
        print("Program Ended")
        break

    else:
        print("Invalid Choice!")