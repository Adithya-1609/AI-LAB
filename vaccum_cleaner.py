def vacuum_cleaner():

    room_A = input("Is Room A dirty? (yes/no): ").lower()
    room_B = input("Is Room B dirty? (yes/no): ").lower()
    current_room = input("Enter the vacuum cleaner's starting room (A/B): ").upper()

    print("\nInitial State:")
    print("Room A:", room_A)
    print("Room B:", room_B)
    print("Vacuum Cleaner is in Room", current_room)

    while room_A == "yes" or room_B == "yes":

        if current_room == "A":
            if room_A == "yes":
                print("\nVacuum cleaner is in Room A.")
                print("Room A is dirty.")
                print("Cleaning Room A...")
                room_A = "no"
                print("Room A is now clean.")

            print("Moving from Room A to Room B...")
            current_room = "B"

        else:
            if room_B == "yes":
                print("\nVacuum cleaner is in Room B.")
                print("Room B is dirty.")
                print("Cleaning Room B...")
                room_B = "no"
                print("Room B is now clean.")


            print("Moving from Room B to Room A...")
            current_room = "A"

    print("\n==============================")
    print("Both rooms are clean!")
    print("Goal state reached.")
    print("==============================")

vacuum_cleaner()
