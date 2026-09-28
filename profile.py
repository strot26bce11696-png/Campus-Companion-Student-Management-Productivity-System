def student_profile():
    while True:
        print("\n--- STUDENT PROFILE ---")
        print("1. Create / Update Profile")
        print("2. View Profile")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            name = input("Enter your name: ")
            roll_no = input("Enter your roll number: ")
            branch = input("Enter your branch: ")

            with open("student_profile.txt", "w") as file:
                file.write("CAMPUS COMPANION - STUDENT PROFILE\n")
                file.write("----------------------------------\n")
                file.write("Name: " + name + "\n")
                file.write("Roll No: " + roll_no + "\n")
                file.write("Branch: " + branch + "\n")

            print("\nProfile saved successfully!")

        elif choice == "2":

            try:
                with open("student_profile.txt", "r") as file:
                    data = file.read()

                print("\n" + data)

            except FileNotFoundError:
                print("\nNo profile found.")
                print("Please create your profile first.")

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")
