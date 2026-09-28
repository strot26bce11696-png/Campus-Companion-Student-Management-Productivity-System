def view_saved_data():
    print("\n--- SAVED DATA ---")

    print("\n1. Student Profile")
    print("2. Attendance")
    print("3. Marks")
    print("4. Tasks")
    print("5. Back")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        filename = "student_profile.txt"

    elif choice == "2":
        filename = "attendance.txt"

    elif choice == "3":
        filename = "marks.txt"

    elif choice == "4":
        filename = "tasks.txt"

    elif choice == "5":
        return

    else:
        print("\nInvalid choice.")
        return

    try:
        with open(filename, "r") as file:
            data = file.read()

        print("\n----------------------------")
        print(data)
        print("----------------------------")

    except FileNotFoundError:
        print("\nNo saved data found.")
        print("Please use that module first.")
