# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   Tom Lowder,11/10/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json
# Define the program's data constants
FILE_NAME: str = "MyLabData.json"
MENU ="""
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
"""
# Define the program's data variables
student_first_name: str = ""
student_last_name: str = ""
student_gpa: float = 0.0
menu_choice: str = ""
student_data: dict = {}
students: list = []
file_data: str = ""
file = None

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
#file = open(FILE_NAME, "r")
#for row in file.readlines():
#    # Transform the data from the file
#   student_data = row.split(",")
#    student_data = {"FirstName": student_data[0],"LastName": student_data[1], "GPA": float(student_data[2].strip())}
#    # Load it into the collection
#    students.append(student_data)
#file.close()
# Repeat the follow tasks
try:

    file = open(FILE_NAME,"r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("--Technical Error Message--")
    print(e,e.__doc__, type(e), sep="\n")
except Exception as e:
    print("There was a non-specific error!")
    print("--Technical Error Message--")
    print(e,e.__doc__, type(e), sep="\n")
finally:
    if file.closed == False:
        file.close()

while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number:")
    print()
    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"
            print(message.format(student["FirstName"],student["LastName"],student["GPA"]))
        print("-"*50)
        continue
    # display the table's current data
    elif menu_choice == "2":
        # Input the data
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            try:
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")
        # add data to the table
            student_data = {"FirstName": student_first_name,"LastName": student_last_name,"GPA":student_gpa}
            students.append(student_data)
        except ValueError as e:
            print(e)
            print("--Technical Error Message--")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("--Technical Error Message--")
            print(e, e.__doc__,type(e), sep="\n")
        continue
    # Save the data to the file
    elif menu_choice == "3":
        #file = open(FILE_NAME,"w")
        #for student in students:
        #    file.write(f"{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n")
        #file.close()
        #print("Data Saved!")
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("--Technical Error Message--")
            print(e,e.__doc__,type(e),sep="\n")
        finally:
            if file.closed == False:
                file.close()
        # Exit the program
    else:
        break
