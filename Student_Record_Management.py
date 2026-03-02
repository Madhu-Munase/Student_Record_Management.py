# Student Record Management System

students = []   # List to store student records


# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# Function to add student
def add_student():
    name = input("Enter Student Name: ")
    roll = int(input("Enter Roll Number: "))

    # Check duplicate roll number
    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!\n")
            return

    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to view students
def view_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    for student in students:
        print("-----------------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
    print()


# Function to search student
def search_student():
    roll = int(input("Enter Roll Number to search: "))

    for student in students:
        if student["roll"] == roll:
            print("Student Found:")
            print("-----------------------------")
            print("Name:", student["name"])
            print("Roll:", student["roll"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", round(student["average"], 2))
            print("Grade:", student["grade"])
            print()
            return

    print("Student not found.\n")


# Function to show class statistics
def class_statistics():
    if len(students) == 0:
        print("No student records available.\n")
        return

    total_students = len(students)

    total_average_sum = 0
    totals = []

    for student in students:
        total_average_sum += student["average"]
        totals.append(student["total"])

    class_average = total_average_sum / total_students
    highest = max(totals)
    lowest = min(totals)

    print("----- Class Statistics -----")
    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Highest Total Marks:", highest)
    print("Lowest Total Marks:", lowest)
    print()


# Main Menu
while True:
    print("===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_statistics()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")