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
            file.write(
                "Attendance: "
                + str(round(percentage, 2))
                + "%\n"
            )
            file.write("Status: " + status + "\n")

            total_classes += total
            total_attended += attended

        overall = (total_attended / total_classes) * 100

        file.write(
            "\nOverall Attendance: "
            + str(round(overall, 2))
            + "%\n"
        )

    print("\n----------------------------")
    print("Overall Attendance:",
          round(overall, 2), "%")
    print("----------------------------")

    if overall >= 75:
        print("Overall Status: Good")
    else:
        print("Overall Status: Attendance is low")

    print("\nAttendance saved successfully!")
