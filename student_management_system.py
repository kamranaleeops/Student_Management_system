import json

FILE_NAME = "students.json"


# ---------------- FILE HANDLING ---------------- #

def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


students = load_students()


# ---------------- HELPER FUNCTION ---------------- #

def find_student(roll):
    for student in students:
        if student["roll"] == roll:
            return student
    return None


# ---------------- CORE FEATURES ---------------- #

def add_student():
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ").strip()

    if find_student(roll):
        print("Student with this roll number already exists!\n")
        return

    name = input("Enter Name: ").strip()
    course = input("Enter Course: ").strip()

    if not name or not course:
        print("Name and Course cannot be empty.\n")
        return

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)
    save_students()

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

    roll = input("Enter Roll Number: ").strip()
    student = find_student(roll)

    if student:
        print("\nStudent Found")
        print("Name:", student["name"])
        print("Course:", student["course"])
        print()
    else:
        print("Student not found.\n")


def update_student():
    print("\n--- Update Student ---")

    roll = input("Enter Roll Number: ").strip()
    student = find_student(roll)

    if not student:
        print("Student not found.\n")
        return

    print("Leave blank to keep current value")

    name = input(f"New Name ({student['name']}): ").strip()
    course = input(f"New Course ({student['course']}): ").strip()

    if name:
        student["name"] = name
    if course:
        student["course"] = course

    save_students()

    print("Student updated successfully!\n")


def delete_student():
    print("\n--- Delete Student ---")

    roll = input("Enter Roll Number: ").strip()
    student = find_student(roll)

    if not student:
        print("Student not found.\n")
        return

    confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ")

    if confirm.lower() == "y":
        students.remove(student)
        save_students()
        print("Student deleted successfully!\n")
    else:
        print("Deletion cancelled.\n")


def sort_students():
    print("\n--- Students Sorted by Name ---")

    if not students:
        print("No students found.\n")
        return

    sorted_students = sorted(students, key=lambda x: x["name"].lower())

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

        choice = input("Enter your choice: ").strip()

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
