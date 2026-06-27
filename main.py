students = {}

def add_student():
    usn = input("Enter Student USN: ").lower()
    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    students[usn] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No students found.\n")
        return

    print("\nStudent Records:")
    print("-" * 30)

    for usn, details in students.items():
        print(f"USN   : {usn}")
        print(f"Name  : {details['name']}")
        print(f"Marks : {details['marks']}")
        print("-" * 30)


def search_student():
    usn = input("Enter USN to search: ").lower()

    if usn in students:
        print("\nStudent Found!")
        print(f"Name  : {students[usn]['name']}")
        print(f"Marks : {students[usn]['marks']}\n")
    else:
        print("Student not found!\n")


def delete_student():
    usn = input("Enter USN to delete: ").lower()

    if usn in students:
        del students[usn]
        print("Student deleted successfully!\n")
    else:
        print("Student not found!\n")


while True:
    print("===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.\n")
