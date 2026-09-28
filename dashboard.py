def dashboard():
    print("\n================================")
    print("       STUDENT DASHBOARD")
    print("================================")

    # Student Profile
    try:
        with open("student_profile.txt", "r") as file:
            profile = file.read()

        print("\n--- PROFILE ---")
        print(profile)

    except FileNotFoundError:
        print("\nProfile: Not available")

    # Attendance
    try:
        with open("attendance.txt", "r") as file:
            attendance_data = file.read()

        print("\n--- ATTENDANCE ---")

        for line in attendance_data.splitlines():
            if line.startswith("Overall Attendance:"):
                print(line)

    except FileNotFoundError:
        print("Attendance: Not available")

    # Marks
    try:
        with open("marks.txt", "r") as file:
            marks_data = file.read()

        print("\n--- MARKS ---")

        for line in marks_data.splitlines():
            if line.startswith("Overall Percentage:"):
                print(line)

    except FileNotFoundError:
        print("Marks: Not available")

    # Tasks
    try:
        with open("tasks.txt", "r") as file:
            tasks_data = file.readlines()

        pending = 0
        completed = 0

        for line in tasks_data:
            if "Status: Pending" in line:
                pending += 1
            elif "Status: Completed" in line:
                completed += 1

        print("\n--- TASK SUMMARY ---")
        print("Pending Tasks:", pending)
        print("Completed Tasks:", completed)

    except FileNotFoundError:
        print("Tasks: Not available")

    print("\n================================")
