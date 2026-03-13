student_management_system
import json

FILE_NAME = "students.json"


# ---------------- FILE HANDLING ---------------- #

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


# ---------------- CORE FEATURES ---------------- #

def add_student():
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ")

    # Prevent duplicate roll numbers
    for s in students:
        if s["roll"] == roll:
            print("Student with this roll number already exists!\n")
            return

    name = input("Enter Name: ")
    course = input("Enter Course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!\n")


def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No students found.\n")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. Name   : {s['name']}")
        print(f"   Roll   : {s['roll']}")
        print(f"   Course : {s['course']}")
        print("--------------------------------")


def search_student():
    print("\n--- Search Student ---")

    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found")
            print("Name:", s["name"])
            print("Course:", s["course"])
            print()
            return

    print("Student not found.\n")


def update_student():
    print("\n--- Update Student ---")

    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("Leave blank to keep current value")

            name = input(f"New Name ({s['name']}): ")
            course = input(f"New Course ({s['course']}): ")

            if name:
                s["name"] = name
            if course:
                s["course"] = course

            save_students(students)

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


def delete_student():
    print("\n--- Delete Student ---")

    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            save_students(students)

            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def sort_students():
    print("\n--- Sort Students by Name ---")

    if not students:
        print("No students found.\n")
        return

    sorted_students = sorted(students, key=lambda x: x["name"])

    for s in sorted_students:
        print(f"Name: {s['name']} | Roll: {s['roll']} | Course: {s['course']}")


def total_students():
    print(f"\nTotal Students: {len(students)}\n")


# ---------------- MENU ---------------- #

def menu():
    while True:
        print("\n========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Sort Students by Name")
        print("7. Total Students")
        print("8. Exit")
        print("===============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            total_students()
        elif choice == "8":
            print("Program exited.")
            break
        else:
            print("Invalid choice.\n")


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    menu()
