# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Tom Lowder,11/19/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Variables
menu_choice: str = ""
students: list = []

# File Processing Class -----------------------------------------#
class FileProcessor:
    """
    Class of functions that process JSON file data

    ChangeLog: (Who, When, What)
    Tom Lowder,11.19.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ Function reads data from a JSON file and loads it into a list of list table

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :param file_name: string data = file name to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: student_data list
        """

        try:
            file_name = open(FILE_NAME, "r")
            student_data = json.load(file_name)
            file_name.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file_name.closed == False:
                file_name.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ Function writes data to JSON file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :param file_name: string data = file name to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            file_name = open(FILE_NAME, "w")
            json.dump(student_data, file_name)
            file_name.close()
            print("The following data has been saved:")
            IO.output_student_courses(student_data=students)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file_name.closed == False:
                file_name.close()


# Presentation --------------------------------------- #
class IO:
    """
    Class of functions that manage user input and output

    ChangeLog: (Who, When, What)
    Tom Lowder,11.19.2024,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ Function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Tom Loder,11.19.2024,Created function

        :param message: string data = message data to display
        :param error: Exception with technical message

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ Function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ Function gets menu choice input from the user

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :return: menu_choice string
        """
        choice = "0"
        try:
            choice = input("What would you like to do: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ Function outputs the student and course names to the user

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ Function gets the student's first name, last name, and a course name from the user

        ChangeLog: (Who, When, What)
        Tom Lowder,11.19.2024,Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Enter the course name: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the incorrect type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Main Body
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        "Data Saved"
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

print("Program Ended")
