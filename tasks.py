def tasks():
    print("\n--- TASK MANAGER ---")

    task_list = []

    number = int(
        input("How many tasks do you want to add? ")
    )

    for i in range(number):
        print("\nTask", i + 1)

        task = input("Enter task: ")
        priority = input(
            "Enter priority (High/Medium/Low): "
        )

        task_data = {
            "task": task,
            "priority": priority,
            "status": "Pending"
        }

        task_list.append(task_data)

    with open("tasks.txt", "w") as file:
        file.write("CAMPUS COMPANION - TASKS\n")
        file.write("----------------------------------\n")

        for i in range(len(task_list)):
            file.write(
                str(i + 1)
                + ". "
                + task_list[i]["task"]
                + " | Priority: "
                + task_list[i]["priority"]
                + " | Status: "
                + task_list[i]["status"]
                + "\n"
            )

    while True:
        print("\n--- YOUR TASKS ---")

        for i in range(len(task_list)):
            print(
                i + 1,
                ".",
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

                task_list[
                    task_number - 1
                ]["status"] = "Completed"

                print("\nTask marked as completed!")

                with open("tasks.txt", "w") as file:
                    file.write(
                        "CAMPUS COMPANION - TASKS\n"
                    )
                    file.write(
                        "----------------------------------\n"
                    )

                    for i in range(len(task_list)):
                        file.write(
                            str(i + 1)
                            + ". "
                            + task_list[i]["task"]
                            + " | Priority: "
                            + task_list[i]["priority"]
                            + " | Status: "
                            + task_list[i]["status"]
                            + "\n"
                        )

            else:
                print("\nInvalid task number.")

        elif choice == "2":
            break

        else:
            print("\nInvalid choice.")
