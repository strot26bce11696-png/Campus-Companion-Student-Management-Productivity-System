from menu import show_menu
from profile import student_profile
from attendance import attendance
from marks import marks
from timetable import timetable
from tasks import tasks
from dashboard import dashboard
from saved_data import view_saved_data


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
        view_saved_data()

    elif choice == "7":
        dashboard()

    elif choice == "8":
        print("\nThank you for using Campus Companion!")
        break

    else:
        print("\nInvalid choice. Please try again")
