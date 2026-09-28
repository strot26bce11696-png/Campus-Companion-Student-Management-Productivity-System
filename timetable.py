def timetable():
    print("\n--- WEEKLY TIMETABLE ---")

    timetable_data = {
        "Monday": [
            "Python",
            "Mathematics",
            "Physics"
        ],
        "Tuesday": [
            "Chemistry",
            "Python Lab",
            "Mathematics"
        ],
        "Wednesday": [
            "Physics",
            "Python",
            "English"
        ],
        "Thursday": [
            "Mathematics",
            "Chemistry",
            "Python Lab"
        ],
        "Friday": [
            "Python",
            "Physics",
            "Mathematics"
        ]
    }

    for day, subjects in timetable_data.items():
        print("\n" + day)
        print("----------------------------")

        for i in range(len(subjects)):
            print(i + 1, ".", subjects[i])
