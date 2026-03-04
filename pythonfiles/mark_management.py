import pandas as pd
import os

def add_student():
    new_roll = input("Enter roll number: ")
    new_name = input("Enter name: ")
    new_age = input("Enter age: ")
    new_marks = input("Enter marks: ")

    new_data = {
        'Roll Number': [new_roll],
        'Name': [new_name],
        'Age': [new_age],
        'Marks': [new_marks]
    }

    new_df = pd.DataFrame(new_data)

    file_name = "std_info.xlsx"

    df = pd.read_excel(file_name)
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_excel(file_name, index=False)
    
    print("Student marks added successfully.")


def view_students():
    file_name = "std_info.xlsx"
    
    df = pd.read_excel(file_name)
    print(df)


def delete_student():
    roll_to_delete = input("Enter roll number to delete: ")

    file_name = "std_info.xlsx"
    
    df = pd.read_excel(file_name)
    df = df[df['Roll Number'] != roll_to_delete]
    df.to_excel(file_name, index=False)
    
    print("Student record deleted successfully.")   

print("Welcome to Student Marks Management System  "    )
print ("Enter 1 to Add Student Marks  \n Enter 2 to View Student Marks \n Enter 3 to Delete Student Marks /n Enter 4 to Exit")
choice = input("Enter your choice (1/2/3/4): ")
while choice != '4':
 if choice == '1':
    add_student()
    choice = input("Enter your choice (1/2/3/4): ")
 elif choice == '2':
    view_students()
    choice = input("Enter your choice (1/2/3/4): ")
 elif choice == '3':
    delete_student()
    choice = input("Enter your choice (1/2/3/4): ")
 else:
    print("Invalid choice. Please enter 1, 2, or 3.")
    choice = input("Enter your choice (1/2/3/4): ")
print("Exiting the program.")
