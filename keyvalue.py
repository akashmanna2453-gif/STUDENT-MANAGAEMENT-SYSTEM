import json
import os


FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)




def display_header(title):
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def pause():
    input("\nPress Enter to continue...")




def student_exists(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return True
    return False


def add_student(students):
    display_header("ADD STUDENT")

    roll_no = input("Enter Roll Number: ").strip()

    if student_exists(students, roll_no):
        print("Student with this Roll Number already exists.")
        return

    name = input("Enter Name: ").strip()
    age = int(input("Enter Age: "))
    course = input("Enter Course: ").strip()
    email = input("Enter Email: ").strip()

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "marks": []
    }

    students.append(student)
    save_data(students)

    print("\nStudent added successfully!")


def display_students(students):
    display_header("ALL STUDENTS")

    if not students:
        print("No students found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print("-" * 40)
        print("Roll Number :", student["roll_no"])
        print("Name        :", student["name"])
        print("Age         :", student["age"])
        print("Course      :", student["course"])
        print("Email       :", student["email"])
        print("Marks       :", student["marks"])


def search_student(students):
    display_header("SEARCH STUDENT")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("-" * 40)
            print("Roll Number :", student["roll_no"])
            print("Name        :", student["name"])
            print("Age         :", student["age"])
            print("Course      :", student["course"])
            print("Email       :", student["email"])
            print("Marks       :", student["marks"])
            return

    print("Student not found.")


def update_student(students):
    display_header("UPDATE STUDENT")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nLeave input empty to keep old value.\n")

            name = input(f"Name [{student['name']}]: ").strip()
            age = input(f"Age [{student['age']}]: ").strip()
            course = input(f"Course [{student['course']}]: ").strip()
            email = input(f"Email [{student['email']}]: ").strip()

            if name:
                student["name"] = name

            if age:
                student["age"] = int(age)

            if course:
                student["course"] = course

            if email:
                student["email"] = email

            save_data(students)

            print("\nStudent updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    display_header("DELETE STUDENT")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:

            confirm = input(
                f"Are you sure you want to delete {student['name']}? (y/n): "
            ).lower()

            if confirm == "y":
                students.remove(student)
                save_data(students)
                print("Student deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Student not found.")




def add_marks(students):
    display_header("ADD MARKS")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            print(f"\nAdding marks for {student['name']}")

            subject_count = int(input("How many subjects? "))

            marks = []

            for i in range(subject_count):
                mark = float(input(f"Enter marks for subject {i + 1}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                else:
                    print("Invalid marks. Enter between 0 and 100.")
                    return

            student["marks"] = marks

            save_data(students)

            print("Marks added successfully!")
            return

    print("Student not found.")


def calculate_average(marks):
    if not marks:
        return 0

    return sum(marks) / len(marks)


def display_result(students):
    display_header("STUDENT RESULT")

    roll_no = input("Enter Roll Number: ").strip()

    for student in students:

        if student["roll_no"] == roll_no:

            marks = student["marks"]

            if not marks:
                print("No marks available.")
                return

            average = calculate_average(marks)

            print("\nName    :", student["name"])
            print("Roll No :", student["roll_no"])
            print("Marks   :", marks)
            print("Average :", round(average, 2))

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            print("Grade   :", grade)

            if average >= 40:
                print("Status  : PASS")
            else:
                print("Status  : FAIL")

            return

    print("Student not found.")



def sort_by_name(students):
    display_header("STUDENTS SORTED BY NAME")

    if not students:
        print("No students available.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student["name"].lower()
    )

    for student in sorted_students:
        print(
            student["roll_no"],
            "-",
            student["name"],
            "-",
            student["course"]
        )


def sort_by_average(students):
    display_header("STUDENTS SORTED BY AVERAGE")

    students_with_marks = []

    for student in students:

        average = calculate_average(student["marks"])

        students_with_marks.append(
            (student, average)
        )

    students_with_marks.sort(
        key=lambda item: item[1],
        reverse=True
    )

    for student, average in students_with_marks:
        print(
            f"{student['name']} -> Average: {average:.2f}"
        )




def show_statistics(students):
    display_header("STATISTICS")

    if not students:
        print("No student data available.")
        return

    total_students = len(students)

    total_marks = 0
    students_with_marks = 0

    highest_average = -1
    topper = None

    for student in students:

        marks = student["marks"]

        if marks:
            average = calculate_average(marks)

            total_marks += average
            students_with_marks += 1

            if average > highest_average:
                highest_average = average
                topper = student

    print("Total Students :", total_students)

    if students_with_marks > 0:

        overall_average = (
            total_marks / students_with_marks
        )

        print(
            "Overall Average:",
            round(overall_average, 2)
        )

        print(
            "Topper         :",
            topper["name"]
        )

        print(
            "Topper Average :",
            round(highest_average, 2)
        )

    else:
        print("No marks available.")


def search_by_course(students):
    display_header("SEARCH BY COURSE")

    course = input("Enter course: ").strip().lower()

    found = False

    for student in students:

        if student["course"].lower() == course:

            print(
                student["roll_no"],
                "-",
                student["name"]
            )

            found = True

    if not found:
        print("No students found for this course.")




def show_menu():
    print("\n")
    print("=" * 60)
    print("STUDENT MANAGEMENT SYSTEM".center(60))
    print("=" * 60)

    print("1.  Add Student")
    print("2.  Display Students")
    print("3.  Search Student")
    print("4.  Update Student")
    print("5.  Delete Student")
    print("6.  Add Marks")
    print("7.  Display Result")
    print("8.  Sort by Name")
    print("9.  Sort by Average")
    print("10. Search by Course")
    print("11. Show Statistics")
    print("12. Exit")

    print("=" * 60)


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

def main():

    students = load_data()

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            add_marks(students)

        elif choice == "7":
            display_result(students)

        elif choice == "8":
            sort_by_name(students)

        elif choice == "9":
            sort_by_average(students)

        elif choice == "10":
            search_by_course(students)

        elif choice == "11":
            show_statistics(students)

        elif choice == "12":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")

        pause()




if __name__ == "__main__":
    main()
