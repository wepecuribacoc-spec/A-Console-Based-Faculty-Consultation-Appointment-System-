# =========================================================
# FACULTY CONSULTATION APPOINTMENT SCHEDULER
# ITE 260 - Computer Programming 1
# =========================================================

from datetime import datetime, date


# =========================================================
# DATA STRUCTURES
# =========================================================

# List of available teachers
faculty_list = [
    "Maam Gwayne",
    "Maam Gly",
    "Sir Ian",
    "Maam Rachel",
    "Sir Alein",
    "Sir Marte"
]


# Each teacher has their own available days and times.
# These are SAMPLE schedules.
# Change them according to the actual schedule of each teacher.

teacher_schedule = {

    "Maam Gwayne": {
        "days": ["Monday", "Wednesday", "Friday"],
        "times": ["9:00 AM", "10:00 AM", "1:00 PM"]
    },

    "Maam Gly": {
        "days": ["Tuesday", "Thursday"],
        "times": ["9:00 AM", "11:00 AM", "2:00 PM"]
    },

    "Sir Ian": {
        "days": ["Monday", "Wednesday"],
        "times": ["10:00 AM", "1:00 PM", "3:00 PM"]
    },

    "Maam Rachel": {
        "days": ["Tuesday", "Thursday", "Friday"],
        "times": ["9:00 AM", "1:00 PM", "2:00 PM"]
    },

    "Sir Alein": {
        "days": ["Monday", "Tuesday", "Thursday"],
        "times": ["10:00 AM", "1:00 PM", "3:00 PM"]
    },

    "Sir Marte": {
        "days": ["Wednesday", "Thursday", "Friday"],
        "times": ["9:00 AM", "11:00 AM", "2:00 PM"]
    }
}


# List that stores all appointment records
appointment_records = []


def display_faculty():

    print("\n===== AVAILABLE TEACHERS =====")

    for i, faculty in enumerate(faculty_list, start=1):
        print(f"{i}. {faculty}")


# =========================================================
# SELECT FACULTY
# =========================================================

def select_faculty():

    while True:

        display_faculty()

        choice = input("Select teacher number: ").strip()

        if choice == "":

            print(
                "[ERROR] Selection cannot be empty."
            )

            continue

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(faculty_list):

                faculty_name = faculty_list[choice - 1]

                print(f"\nSelected Teacher: {faculty_name}")

                print("Available Days:")

                for day in teacher_schedule[faculty_name]["days"]:
                    print(f"- {day}")

                print("Available Times:")

                for time in teacher_schedule[faculty_name]["times"]:
                    print(f"- {time}")

                return faculty_name

            else:

                print(
                    "[ERROR] Invalid teacher selection. Please choose a number from the list."
                )

        else:

            print(
                "[ERROR] Please enter a valid number."
            )


# =========================================================
# GET DAY OF THE WEEK
# =========================================================

def get_day_of_week(date_text):

    try:

        date_object = datetime.strptime(
            date_text,
            "%Y-%m-%d"
        )

        return date_object.strftime("%A")

    except ValueError:

        return None


# =========================================================
# SELECT DATE
# =========================================================
# IMPORTANT:
# The user will remain in this function until a valid
# future date matching the teacher's available day is entered.
# =========================================================

def select_date(faculty_name):

    print("\n===== FACULTY AVAILABLE DAYS =====")

    available_days = teacher_schedule[faculty_name]["days"]

    for i, day in enumerate(available_days, start=1):
        print(f"{i}. {day}")

    today = date.today()

    print("\nEnter the consultation date.")
    print("Format: YYYY-MM-DD")
    print(f"Example: {today.year}-10-02")

    # Keep asking until a valid date is entered
    while True:

        appointment_date = input(
            "\nEnter exact date: "
        ).strip()


        # ---------------------------------------------
        # CHECK IF EMPTY
        # ---------------------------------------------

        if appointment_date == "":

            print(
                "[WARNING] Date cannot be empty."
            )

            print(
                "Please enter a new date."
            )

            continue


        # ---------------------------------------------
        # CHECK IF DATE CONTAINS LETTERS / WORDS
        # ---------------------------------------------

        if any(char.isalpha() for char in appointment_date):

            print(
                "\n[WARNING] Date cannot contain letters or words."
            )

            print(
                "Letters and words are not allowed."
            )

            print(
                "Please enter numbers only using YYYY-MM-DD format."
            )

            print(
                f"Example: {today.year}-10-02"
            )

            continue


        # ---------------------------------------------
        # CHECK DATE FORMAT & CALENDAR VALIDITY
        # ---------------------------------------------

        try:

            selected_date = datetime.strptime(
                appointment_date,
                "%Y-%m-%d"
            ).date()

        except ValueError:

            print(
                "\n[WARNING] Invalid date format or calendar date."
            )

            print(
                "Please use the format YYYY-MM-DD."
            )

            print(
                f"Example: {today.year}-10-02"
            )

            continue


        # ---------------------------------------------
        # CHECK IF DATE IS OLD
        # ---------------------------------------------

        if selected_date < today:

            print(
                "\n[WARNING] The date you entered "
                "has already passed."
            )

            print(
                f"Today is {today.strftime('%Y-%m-%d')}."
            )

            print(
                "Please enter a new future date."
            )

            # Stay here instead of returning to menu
            continue


        # ---------------------------------------------
        # CHECK IF YEAR IS IN THE FUTURE
        # ---------------------------------------------

        if selected_date.year > today.year:

            print(
                f"\n[WARNING] Invalid year. You cannot select a future year ({selected_date.year})."
            )

            print(
                f"The maximum selectable year is {today.year}."
            )

            print(
                f"Please enter a date within the current year ({today.year})."
            )

            # Stay here instead of returning to menu
            continue


        # ---------------------------------------------
        # CHECK TEACHER'S AVAILABLE DAY
        # ---------------------------------------------

        day_name = selected_date.strftime("%A")


        if day_name not in available_days:

            print(
                f"\n[WARNING] {faculty_name} is not "
                f"available on {day_name}."
            )

            print(
                "Available days:",
                ", ".join(available_days)
            )

            print(
                "Please enter another date."
            )

            # Stay here instead of returning to menu
            continue


        # ---------------------------------------------
        # VALID DATE
        # ---------------------------------------------

        print(
            f"\n[SUCCESS] {appointment_date} "
            f"is available."
        )

        return appointment_date


# =========================================================
# SELECT TIME
# =========================================================

def select_time(faculty_name):

    print("\n===== AVAILABLE TIMES =====")

    available_times = teacher_schedule[faculty_name]["times"]

    for i, time in enumerate(available_times, start=1):
        print(f"{i}. {time}")

    # Keep asking until a valid time is selected
    while True:

        choice = input(
            "Select time number: "
        ).strip()


        # ---------------------------------------------
        # CHECK IF EMPTY
        # ---------------------------------------------

        if choice == "":

            print(
                "[WARNING] Selection cannot be empty."
            )

            continue


        # ---------------------------------------------
        # CHECK IF NUMBER
        # ---------------------------------------------

        if choice.isdigit():

            choice = int(choice)

            if 1 <= choice <= len(available_times):

                return available_times[choice - 1]

            else:

                print(
                    "[WARNING] Invalid time selection."
                )

                print(
                    "Please choose one of the available times."
                )

        else:

            print(
                "[WARNING] Please enter a valid number."
            )


# =========================================================
# CHECK SCHEDULE CONFLICT
# =========================================================

def check_conflict(
    faculty_name,
    appointment_date,
    appointment_time,
    exclude_id=None
):

    for record in appointment_records:

        # Exclude specific appointment (e.g. during reschedule)
        if exclude_id is not None and record[0] == exclude_id:
            continue

        same_faculty = record[3] == faculty_name

        same_date = record[4] == appointment_date

        same_time = record[5] == appointment_time

        active_status = record[7] != "Cancelled"


        if (
            same_faculty
            and same_date
            and same_time
            and active_status
        ):

            return True


    return False


# =========================================================
# CREATE APPOINTMENT
# =========================================================

def create_appointment(
    student_id,
    student_name,
    faculty_name,
    appointment_date,
    appointment_time,
    purpose
):

    appointment_id = len(appointment_records) + 1

    status = "Pending"


    record = [

        appointment_id,

        student_id,

        student_name,

        faculty_name,

        appointment_date,

        appointment_time,

        purpose,

        status

    ]


    appointment_records.append(record)

    return record


# =========================================================
# DISPLAY APPOINTMENTS
# HORIZONTAL TABLE
# =========================================================

def display_appointments(records=None):

    if records is None:

        records = appointment_records


    print("\n" + "=" * 145)

    print(
        f"{'ID':<5}"
        f"{'Student ID':<14}"
        f"{'Student Name':<18}"
        f"{'Teacher':<16}"
        f"{'Date':<13}"
        f"{'Time':<11}"
        f"{'Purpose':<30}"
        f"{'Status':<15}"
    )

    print("-" * 145)


    if len(records) == 0:

        print(
            "No appointment records found."
        )

    else:

        for record in records:

            print(
                f"{record[0]:<5}"
                f"{record[1]:<14}"
                f"{record[2]:<18}"
                f"{record[3]:<16}"
                f"{record[4]:<13}"
                f"{record[5]:<11}"
                f"{record[6]:<30}"
                f"{record[7]:<15}"
            )


    print("=" * 145)


# =========================================================
# FIND APPOINTMENT
# =========================================================

def find_appointment(appointment_id):

    for record in appointment_records:

        if record[0] == appointment_id:

            return record


    return None


# =========================================================
# STUDENT ID VALIDATION
# =========================================================

def get_student_id():

    while True:

        student_id = input(
            "Enter Student ID: "
        ).strip()


        if student_id == "":

            print(
                "[WARNING] Student ID cannot be empty."
            )

            continue


        # Allow numbers and dashes only (example: 2026-12345).
        # The ID must contain at least one number.
        if not all(char.isdigit() or char == "-" for char in student_id) or not any(char.isdigit() for char in student_id):

            print(
                "[WARNING] Student ID can contain numbers and dashes only."
            )

            print(
                "Example: 2026-12345"
            )

            continue


        return student_id


# =========================================================
# STUDENT APPOINTMENT REQUEST
# =========================================================

def student_appointment_request():

    print("\n========================================")
    print("       STUDENT APPOINTMENT REQUEST")
    print("========================================")


    # Student ID
    student_id = get_student_id()


    # Student Name
    while True:

        student_name = input(
            "Enter Student Name: "
        ).strip()


        if student_name == "":

            print(
                "[WARNING] Student name cannot be empty."
            )

            continue


        # Check for alphabetic characters with optional space, dot, or hyphen
        clean_name = student_name.replace(" ", "").replace(".", "").replace("-", "")

        if not clean_name.isalpha():

            print(
                "[WARNING] Student name must contain letters only."
            )

            print(
                "Numbers and special symbols are not allowed."
            )

            continue


        break


    # Select Teacher
    faculty_name = select_faculty()


    if faculty_name is None:

        return


    # Select Date (with protection against fully booked dates)
    while True:

        appointment_date = select_date(
            faculty_name
        )

        available_times = teacher_schedule[faculty_name]["times"]

        occupied_times = [
            t for t in available_times
            if check_conflict(faculty_name, appointment_date, t)
        ]

        if len(occupied_times) >= len(available_times):

            print(
                f"\n[WARNING] All consultation time slots for {faculty_name} "
                f"on {appointment_date} are already fully booked."
            )

            print(
                "Please choose another date."
            )

            continue

        break


    # Select Time
    appointment_time = select_time(
        faculty_name
    )


    # Check Schedule Conflict
    while check_conflict(
        faculty_name,
        appointment_date,
        appointment_time
    ):

        print(
            "\n[WARNING] The selected schedule "
            "is already occupied."
        )

        print(
            "Please choose another time."
        )

        appointment_time = select_time(
            faculty_name
        )


    # Purpose
    while True:

        purpose = input(
            "Enter Purpose of Consultation: "
        ).strip()


        if purpose == "":

            print(
                "[WARNING] Purpose cannot be empty."
            )

            continue


        if not any(char.isalpha() for char in purpose):

            print(
                "[WARNING] Purpose must contain descriptive text/letters."
            )

            continue


        break


    # Create Appointment
    record = create_appointment(

        student_id,

        student_name,

        faculty_name,

        appointment_date,

        appointment_time,

        purpose

    )


    print(
        "\n[SUCCESS] Appointment request submitted!"
    )


    print(
        "\n===== APPOINTMENT DETAILS ====="
    )

    display_appointments([record])


# =========================================================
# STUDENT VIEW APPOINTMENT
# =========================================================

def student_view_appointment():

    print("\n========================================")
    print("          MY APPOINTMENT")
    print("========================================")


    student_id = get_student_id()


    student_records = []


    for record in appointment_records:

        if record[1] == student_id:

            student_records.append(record)


    if len(student_records) == 0:

        print(
            "\n[INFO] No appointment found "
            "for Student ID:",
            student_id
        )

    else:

        print(
            "\n===== YOUR APPOINTMENT RECORDS ====="
        )

        display_appointments(
            student_records
        )


# =========================================================
# STUDENT MENU
# =========================================================

def student_menu():

    while True:

        print("\n========================================")
        print("             STUDENT MENU")
        print("========================================")
        print("[1] Appointment Request")
        print("[2] Appointment View")
        print("[3] View Teacher Schedule")
        print("[4] Exit")
        print("========================================")

        choice = input(
            "Select an option (1-4): "
        ).strip()

        if choice == "1":
            student_appointment_request()

        elif choice == "2":
            student_view_appointment()

        elif choice == "3":
            view_teacher_schedule()

        elif choice == "4":
            print(
                "\nReturning to main menu..."
            )
            break

        else:
            print(
                "[WARNING] Invalid option. "
                "Please choose 1-4."
            )


# =========================================================
# TEACHER ACCEPT APPOINTMENT
# =========================================================

def accept_appointment():

    if len(appointment_records) == 0:

        print(
            "\n[INFO] No appointment records available."
        )

        return


    print(
        "\n===== APPOINTMENT RECORDS ====="
    )

    display_appointments()


    choice = input(
        "\nEnter Appointment ID to accept: "
    ).strip()


    if choice == "":

        print(
            "[WARNING] Appointment ID cannot be empty."
        )

        return


    if not choice.isdigit():

        print(
            "[WARNING] Please enter a valid "
            "appointment ID (numbers only)."
        )

        return


    appointment_id = int(choice)

    record = find_appointment(
        appointment_id
    )


    if record is None:

        print(
            "[WARNING] Appointment not found."
        )


    elif record[7] == "Accepted":

        print(
            "\n[WARNING] Appointment is already accepted."
        )


    elif record[7] in ["Pending", "Rescheduled"]:

        record[7] = "Accepted"

        print(
            "\n[SUCCESS] Appointment accepted."
        )


    elif record[7] == "Cancelled":

        print(
            "[WARNING] Cancelled appointment "
            "cannot be accepted."
        )


    else:

        print(
            "[WARNING] Appointment cannot be accepted "
            "in its current status."
        )


# =========================================================
# TEACHER RESCHEDULE APPOINTMENT
# =========================================================

def reschedule_appointment():

    if len(appointment_records) == 0:

        print(
            "\n[INFO] No appointment records available."
        )

        return


    print(
        "\n===== APPOINTMENT RECORDS ====="
    )

    display_appointments()


    choice = input(
        "\nEnter Appointment ID to reschedule: "
    ).strip()


    if choice == "":

        print(
            "[WARNING] Appointment ID cannot be empty."
        )

        return


    if not choice.isdigit():

        print(
            "[WARNING] Please enter a valid "
            "appointment ID (numbers only)."
        )

        return


    appointment_id = int(choice)

    record = find_appointment(
        appointment_id
    )


    if record is None:

        print(
            "[WARNING] Appointment not found."
        )

        return


    if record[7] == "Cancelled":

        print(
            "[WARNING] Cancelled appointment "
            "cannot be rescheduled."
        )

        return


    faculty_name = record[3]


    # Select new date (with full-booking check)
    while True:

        new_date = select_date(
            faculty_name
        )

        available_times = teacher_schedule[faculty_name]["times"]

        occupied_times = [
            t for t in available_times
            if check_conflict(faculty_name, new_date, t, exclude_id=record[0])
        ]

        if len(occupied_times) >= len(available_times):

            print(
                f"\n[WARNING] All consultation time slots for {faculty_name} "
                f"on {new_date} are already fully booked."
            )

            print(
                "Please choose another date."
            )

            continue

        break


    # Select new time
    new_time = select_time(
        faculty_name
    )


    # Check if schedule is identical to current schedule
    if new_date == record[4] and new_time == record[5]:

        print(
            "\n[WARNING] The new schedule is identical to the current schedule."
        )

        print(
            "No changes were made."
        )

        return


    # Check schedule conflict (excluding current record)
    while check_conflict(
        faculty_name,
        new_date,
        new_time,
        exclude_id=record[0]
    ):

        print(
            "\n[WARNING] The selected schedule "
            "is already occupied."
        )

        print(
            "Please select another time."
        )

        new_time = select_time(
            faculty_name
        )


    # Update appointment
    record[4] = new_date

    record[5] = new_time

    record[7] = "Rescheduled"


    print(
        "\n[SUCCESS] Appointment successfully "
        "rescheduled."
    )


# =========================================================
# TEACHER CANCEL APPOINTMENT
# =========================================================

def cancel_appointment():

    if len(appointment_records) == 0:

        print(
            "\n[INFO] No appointment records available."
        )

        return


    print(
        "\n===== APPOINTMENT RECORDS ====="
    )

    display_appointments()


    choice = input(
        "\nEnter Appointment ID to cancel: "
    ).strip()


    if choice == "":

        print(
            "[WARNING] Appointment ID cannot be empty."
        )

        return


    if not choice.isdigit():

        print(
            "[WARNING] Please enter a valid "
            "appointment ID (numbers only)."
        )

        return


    appointment_id = int(choice)

    record = find_appointment(
        appointment_id
    )


    if record is None:

        print(
            "[WARNING] Appointment not found."
        )


    elif record[7] == "Cancelled":

        print(
            "[WARNING] Appointment is already cancelled."
        )


    else:

        record[7] = "Cancelled"

        print(
            "\n[SUCCESS] Appointment cancelled."
        )


# =========================================================
# VIEW TEACHER SCHEDULE
# =========================================================

def view_teacher_schedule():

    print(
        "\n========================================"
    )

    print(
        "       TEACHER CONSULTATION SCHEDULE"
    )

    print(
        "========================================")


    for faculty in faculty_list:

        print(
            f"\n{faculty}"
        )

        print(
            "Available Days:",
            ", ".join(
                teacher_schedule[faculty]["days"]
            )
        )

        print(
            "Available Times:",
            ", ".join(
                teacher_schedule[faculty]["times"]
            )
        )


# =========================================================
# TEACHER MENU
# =========================================================

def teacher_menu():

    while True:

        print("\n========================================")
        print("             TEACHER MENU")
        print("========================================")
        print("[1] View Appointment Records")
        print("[2] Accept Appointment")
        print("[3] Reschedule Appointment")
        print("[4] Cancel Appointment")
        print("[5] View Teacher Schedule")
        print("[6] Exit")
        print("========================================")

        choice = input(
            "Select an option (1-6): "
        ).strip()

        if choice == "1":
            display_appointments()

        elif choice == "2":
            accept_appointment()

        elif choice == "3":
            reschedule_appointment()

        elif choice == "4":
            cancel_appointment()

        elif choice == "5":
            view_teacher_schedule()

        elif choice == "6":
            print("\nReturning to main menu...")
            break

        else:
            print(
                "[WARNING] Invalid option. "
                "Please choose 1-6."
            )


# =========================================================

# MAIN MENU
# =========================================================

def main():

    while True:

        print("\n" + "=" * 45)

        print(
            "     FACULTY CONSULTATION SCHEDULER"
        )

        print("=" * 45)

        print("[1] Student")
        print("[2] Teacher")
        print("[3] Exit")

        print("=" * 45)


        choice = input(
            "Select an option: "
        ).strip()


        if choice == "1":

            student_menu()


        elif choice == "2":

            teacher_menu()


        elif choice == "3":

            print(
                "\nExiting system. Goodbye!"
            )

            break


        else:

            print(
                "[WARNING] Invalid option. "
                "Please choose 1, 2, or 3."
            )


# =========================================================
# RUN PROGRAM
# =========================================================

if __name__ == "__main__":
    main()