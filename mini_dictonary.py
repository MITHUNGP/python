# Student Management System using Dictionary

students = {}

# Adding students
students["101"] = {"name": "Mithun", "age": 20}
students["102"] = {"name": "Sara", "age": 22}
students["103"] = {"name": "Raj", "age": 19}

print("Students added successfully!")
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Student
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")

        students[roll] = {"name": name, "age": age}
        print(" Student added successfully!")

    # View All Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n All Students:")
            for roll, info in students.items():
                print(f"Roll No: {roll}, Name: {info['name']}, Age: {info['age']}")

    # Search Student
    elif choice == "3":
        roll_no = input("Enter Roll Number to search: ")
        if roll_no in students:
            print(" Student Found:", students[roll_no])
        else:
            print(" Student not found!")

    # Exit
    elif choice == "4":
        print(" Exiting program. Goodbye!")
        break

    else:
        print(" Invalid choice, please enter 1-4.")
