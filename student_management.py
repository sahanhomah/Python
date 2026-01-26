import os
FILE_NAME="sahan.txt"
def add_student():
    roll=input("Enter roll number: ")
    name=input("Enter name: ")
    age=input("Enter age: ")
    with open(FILE_NAME,"a") as file:
        file.write(f"{roll},{name},{age}\n")
    print("Student added successfully.")
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    with open(FILE_NAME,"r") as file:
        students=file.readlines()
        if not students:
            print("No student records found.")
            return
        print("Roll Number | Name | Age")
        for student in students:
            roll,name,age=student.strip().split(",")
            print(f"{roll} | {name} | {age}")
def search_student():
    roll_to_search=input("Enter roll number to search: ")
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    with open(FILE_NAME,"r") as file:
        students=file.readlines()
        found=False
        for student in students:
            roll,name,age=student.strip().split(",")
            if roll==roll_to_search:
                print(f"Student Found: Roll Number: {roll}, Name: {name}, Age: {age}")
                found=True
                break
        if not found:
            print("Student with the given roll number not found.")
def delete_student():   

    roll_to_delete=input("Enter roll number of the student to delete: ")
    if not os.path.exists(FILE_NAME):
        print("No student records found.")
        return
    with open(FILE_NAME,"r") as file:
        students=file.readlines()
    with open(FILE_NAME,"w") as file:
        found=False
        for student in students:
            roll,name,age=student.strip().split(",")
            if roll!=roll_to_delete:
                file.write(student)
            else:
                found=True
        if found:
            print("Student deleted successfully.")
        else:
            print("Student with the given roll number not found.")

def menu():
    while True:
        print("\n===== Student Record Management =====")
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
            print("👋 Exiting Program...")
            break
        else:
            print("⚠ Invalid choice!")

menu()