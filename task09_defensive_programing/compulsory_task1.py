#This code implements a simple calculator that prompts the user to enter two numbers and an operator, 
#then calculates the result of the operation and prints it to the console. 
#The program also writes each equation and its corresponding result to a file named equations.txt.

#The calculate function checks the operator and performs the corresponding operation on the two numbers, 
#returning either the result of the operation or an error message if the operator is invalid or if division by zero is attempted.

#The get_equation function prompts the user to enter the two numbers and the operator, 
#using try-except blocks to handle invalid inputs. It returns the three values as a tuple.

#The write_to_file function checks if the equations.txt file exists and creates it if it doesn't. 
#Then it appends the equation and its result to the end of the file.

#In the main loop, the program gets an equation from the user, calculates the result, 
#prints the equation and result to the console, and writes the equation and result to the equations.txt file. 
#It then prompts the user to continue or quit, and exits the loop and the program if the user chooses to quit.

#If the user chooses to read from file by entering 'r', the function read_from_file will be called, 
#It will then read all the equations and results from the equations.txt file and print them out.


import os

def calculate(first_number, second_number, operator):
    """
    This function takes two numbers and an operator and performs the corresponding operation.
    Returns the result of the operation, or an error message if operation is invalid.
    """
    # check the operator and perform the corresponding operation
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator in ['*', 'x']:
        return first_number * second_number
    elif operator == '/' and second_number == 0:
        # handle division by zero error
        return "Error: Division by zero is not allowed."
    elif operator == '/':
        return first_number / second_number
    else:
        # handle invalid operator error
        return "Error: Invalid operator."

def get_equation():
    """
    This function prompts the user to enter two numbers and an operator, and returns them as a tuple.
    """
    # prompt for first number
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # prompt for second number
    while True:
        try:
            second_number = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # prompt for operator
    while True:
        operator = input("Enter the operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid input. Please enter a valid operator.")

    return first_number, second_number, operator

def write_to_file(filename, equation, result):
    """
    This function writes the equation and its result to a file named by user.
    If the file does not exist, it creates it.
    """
    if not os.path.isfile(filename):
        # create a new file if it does not exist
        with open(filename, 'w') as f:
            pass

    # append the equation and its result to the file
    with open(filename, 'a') as f:
        f.write(f"{equation} = {result}\n")

def read_from_file():
    """
    This function reads all equations and results from a user-specified file and prints them out.
    """
    while True:
        try:
            filename = input("Enter the name of the file to read from: ")
            with open(filename, 'r') as f:
                for line in f:
                    print(line.rstrip())
            break
        except FileNotFoundError:
            print("Error: File not found. Please enter a valid filename.")
        except PermissionError:
            print("Error: You do not have permission to read this file.")
        except:
            print("An error occurred while reading the file.")

def main():
    """Main function that runs the program."""
    print("Welcome to the simple calculator program!")
    
    while True:
        user_choice = input("Enter 'e' to do equations or 'r' to read in equations from a file: ")
        
        if user_choice == 'e':
            filename = input("Enter the name of the file to write equations to: ")
            
            # main loop for doing equations
            while True:
                first_number, second_number, operator = get_equation()
                result = calculate(first_number, second_number, operator)
                equation_str = f"{first_number} {operator} {second_number}"
                print(f"{equation_str} = {result}")
                write_to_file(filename, equation_str, result)

                # prompt for user choice to continue or quit
                while True:
                    try:
                        user_choice = input("Enter 'q' to quit, 'c' to continue, 'rc' to read from a file and continue or 'rq' to read from a file and quit: ")
                        if user_choice in ['q', 'c', 'rc', 'rq']:
                            break
                        else:
                            print("Invalid input. Please enter 'q', 'c', 'rc' or 'rq'.")
                    except ValueError:
                        print("Invalid input. Please enter 'q', 'c', 'rc' or 'rq'.")

                if user_choice == 'q':
                    # exit the program if user chooses to quit
                    return
                elif user_choice == 'rc':
                    # read from file and continue
                    read_from_file()
                elif user_choice == 'rq':
                    # read from file and quit
                    read_from_file()
                    return

        elif user_choice == 'r':
            read_from_file()

if __name__ == "__main__":
    main()
