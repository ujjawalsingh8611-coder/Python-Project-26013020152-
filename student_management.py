FILE_NAME = "students.txt"


def load_students():
    students = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.rstrip("\n").split("|")
                if len(parts) == 4:
                    roll_no, name, course, marks = parts
                    students.append({
                        "roll_no": roll_no,
                        "name": name,
                        "course": course,
                        "marks": float(marks)
                    })
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for student in students:
            file.write(
                f"{student['roll_no']}|{student['name']}|"
                f"{student['course']}|{student['marks']}\n"
            )


def find_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def add_student(students):
    roll_no = input("Enter roll number: ").strip()
    if not roll_no or find_student(students, roll_no):
        print("Invalid or already registered roll number.")
        return

    name = input("Enter student name: ").strip()
    course = input("Enter course/branch: ").strip()
    if not name or not course or "|" in name or "|" in course:
        print("Name and course are required. Do not use the | character.")
        return

    students.append({
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": get_marks()
    })
    save_students(students)
    print("Student record added successfully.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n{:<12} {:<22} {:<18} {:>8}".format(
        "Roll No.", "Name", "Course", "Marks"))
    print("-" * 64)
    for student in students:
        print("{:<12} {:<22} {:<18} {:>8.2f}".format(
            student["roll_no"], student["name"][:21],
            student["course"][:17], student["marks"]))


def search_student(students):
    roll_no = input("Enter roll number to search: ").strip()
    student = find_student(students, roll_no)
    if student:
        print(f"\nName: {student['name']}")
        print(f"Roll number: {student['roll_no']}")
        print(f"Course/Branch: {student['course']}")
        print(f"Marks: {student['marks']:.2f}")
    else:
        print("Student not found.")


def update_student(students):
    roll_no = input("Enter roll number to update: ").strip()
    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return

    name = input(f"New name [{student['name']}]: ").strip()
    course = input(f"New course [{student['course']}]: ").strip()
    if name:
        if "|" in name:
            print("Do not use the | character.")
            return
        student["name"] = name
    if course:
        if "|" in course:
            print("Do not use the | character.")
            return
        student["course"] = course

    change_marks = input("Update marks? (y/n): ").strip().lower()
    if change_marks == "y":
        student["marks"] = get_marks()

    save_students(students)
    print("Student record updated successfully.")


def delete_student(students):
    roll_no = input("Enter roll number to delete: ").strip()
    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return

    confirm = input(f"Delete {student['name']}'s record? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student record deleted.")
    else:
        print("Deletion cancelled.")


def main():
    students = load_students()

    while True:
        print("\n====== STUDENT RECORD MANAGEMENT SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the Student Record Management System!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
