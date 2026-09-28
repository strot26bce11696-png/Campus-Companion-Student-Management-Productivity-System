# ==========================================
#        CAMPUS COMPANION
#   Student Management System
# ==========================================

def show_menu():
    print("\n================================")
    print("       CAMPUS COMPANION")
    print("================================")
    print("1. Student Profile")
    print("2. Attendance")
    print("3. Marks")
    print("4. Timetable")
    print("5. Tasks")
    print("6. Exit")
    print("================================")


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


        def attendance():
    print("\n--- ATTENDANCE ---")

    subjects = int(input("How many subjects do you have? "))

    total_classes = 0
    total_attended = 0

    with open("attendance.txt", "w") as file:
        file.write("CAMPUS COMPANION - ATTENDANCE\n")
        file.write("----------------------------------\n")

        for i in range(subjects):
            print("\nSubject", i + 1)

            subject = input("Enter subject name: ")
            total = int(input("Enter total classes: "))
            attended = int(input("Enter classes attended: "))

            percentage = (attended / total) * 100

            print("Subject:", subject)
            print("Attendance:", round(percentage, 2), "%")

            if percentage >= 75:
                print("Status: Attendance is sufficient")
                status = "Sufficient"
            else:
                print("Status: LOW ATTENDANCE")
                status = "Low"

            file.write("\nSubject: " + subject + "\n")
            file.write("Total Classes: " + str(total) + "\n")
            file.write("Classes Attended: " + str(attended) + "\n")
            file.write("Attendance: " + str(round(percentage, 2)) + "%\n")
            file.write("Status: " + status + "\n")

            total_classes += total
            total_attended += attended

        overall = (total_attended / total_classes) * 100

        file.write("\nOverall Attendance: "
                   + str(round(overall, 2)) + "%\n")

    print("\n----------------------------")
    print("Overall Attendance:",
          round(overall, 2), "%")
    print("----------------------------")

    if overall >= 75:
        print("Overall Status: Good")
    else:
        print("Overall Status: Attendance is low")

    print("\nAttendance saved successfully!")


  def marks():
    print("\n--- MARKS ---")

    subjects = int(input("How many subjects do you have? "))

    total_obtained = 0
    total_marks = 0

    with open("marks.txt", "w") as file:
        file.write("CAMPUS COMPANION - MARKS\n")
        file.write("----------------------------------\n")

        for i in range(subjects):
            print("\nSubject", i + 1)

            subject = input("Enter subject name: ")
            obtained = float(input("Enter marks obtained: "))
            maximum = float(input("Enter total marks: "))

            percentage = (obtained / maximum) * 100

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("Subject:", subject)
            print("Percentage:", round(percentage, 2), "%")
            print("Grade:", grade)

            file.write("\nSubject: " + subject + "\n")
            file.write("Marks: " + str(obtained)
                       + "/" + str(maximum) + "\n")
            file.write("Percentage: "
                       + str(round(percentage, 2)) + "%\n")
            file.write("Grade: " + grade + "\n")

            total_obtained += obtained
            total_marks += maximum

        overall = (total_obtained / total_marks) * 100

        file.write("\nOverall Percentage: "
                   + str(round(overall, 2)) + "%\n")

    print("\n----------------------------")
    print("Overall Percentage:",
          round(overall, 2), "%")
    print("----------------------------")

    print("\nMarks saved successfully!")

def timetable():
    print("\n--- WEEKLY TIMETABLE ---")

    timetable_data = {
        "Monday": ["Python", "Mathematics", "Physics"],
        "Tuesday": ["Chemistry", "Python Lab", "Mathematics"],
        "Wednesday": ["Physics", "Python", "English"],
        "Thursday": ["Mathematics", "Chemistry", "Python Lab"],
        "Friday": ["Python", "Physics", "Mathematics"]
    }

    for day, subjects in timetable_data.items():
        print("\n" + day)
        print("----------------------------")

        for i in range(len(subjects)):
            print(i + 1, ".", subjects[i])


def tasks():
    print("\n--- TASK MANAGER ---")

    task_list = []

    number = int(input("How many tasks do you want to add? "))

    for i in range(number):
        print("\nTask", i + 1)

        task = input("Enter task: ")
        priority = input("Enter priority (High/Medium/Low): ")

        task_data = {
            "task": task,
            "priority": priority,
            "status": "Pending"
        }

        task_list.append(task_data)

    # Save tasks to file
    with open("tasks.txt", "w") as file:
        file.write("CAMPUS COMPANION - TASKS\n")
        file.write("----------------------------------\n")

        for i in range(len(task_list)):
            file.write(
                str(i + 1) + ". " +
                task_list[i]["task"] +
                " | Priority: " +
                task_list[i]["priority"] +
                " | Status: " +
                task_list[i]["status"] +
                "\n"
            )

    while True:
        print("\n--- YOUR TASKS ---")

        for i in range(len(task_list)):
            print(
                i + 1, ".",
                task_list[i]["task"],
                "| Priority:",
                task_list[i]["priority"],
                "| Status:",
                task_list[i]["status"]
            )

        print("\n1. Mark task as completed")
        print("2. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            task_number = int(
                input("Enter task number: ")
            )

            if 1 <= task_number <= len(task_list):

                task_list[task_number - 1]["status"] = "Completed"

                print("\nTask marked as completed!")

                # Update saved file
                with open("tasks.txt", "w") as file:
                    file.write("CAMPUS COMPANION - TASKS\n")
                    file.write("----------------------------------\n")

                    for i in range(len(task_list)):
                        file.write(
                            str(i + 1) + ". " +
                            task_list[i]["task"] +
                            " | Priority: " +
                            task_list[i]["priority"] +
                            " | Status: " +
                            task_list[i]["status"] +
                            "\n"
                        )

            else:
                print("\nInvalid task number.")

        elif choice == "2":
            break

        else:
            print("\nInvalid choice.")


# Main program
while True:

    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        student_profile()

    elif choice == "2":
        attendance()

    elif choice == "3":
        marks()

    elif choice == "4":
        timetable()

    elif choice == "5":
        tasks()

    elif choice == "6":
        print("\nThank you for using Campus Companion!")
        break

    else:
        print("\nInvalid choice. Please try again.")