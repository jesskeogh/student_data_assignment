# this is a test page to ensure this works for my assignment

students = []

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    email = input("Enter email: ")
    student = {"name": name, "grade": grade, "email": email}
    students.append(student)
    print("Student added!")

def view_students():
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} - Grade {s['grade']} - {s['email']}")

while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
