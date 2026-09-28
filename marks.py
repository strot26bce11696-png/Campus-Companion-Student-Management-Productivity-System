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
            file.write(
                "Marks: "
                + str(obtained)
                + "/"
                + str(maximum)
                + "\n"
            )
            file.write(
                "Percentage: "
                + str(round(percentage, 2))
                + "%\n"
            )
            file.write("Grade: " + grade + "\n")

            total_obtained += obtained
            total_marks += maximum

        overall = (total_obtained / total_marks) * 100

        file.write(
            "\nOverall Percentage: "
            + str(round(overall, 2))
            + "%\n"
        )

    print("\n----------------------------")
    print(
        "Overall Percentage:",
        round(overall, 2),
        "%"
    )
    print("----------------------------")

    print("\nMarks saved successfully!")
