# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    
    student = {
        "name": name,
        "roll": roll,
        "course": course
    }
    
    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
    else:
        for s in students:
            print("Name:", s["name"])
            print("Roll:", s["roll"])
            print("Course:", s["course"])
            print("-----------------")


def search_student():
    roll = input("Enter roll number to search: ")
    
    for s in students:
        if s["roll"] == roll:
            print("Student Found")
            print("Name:", s["name"])
            print("Course:", s["course"])
            return
    
    print("Student not found.\n")


def delete_student():
    roll = input("Enter roll number to delete: ")
    
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted.\n")
            return
    
    print("Student not found.\n")


while True:
    print("---- Student Management System ----")
    print("1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program Exit")
        break
    else:
        print("Invalid choice\n")