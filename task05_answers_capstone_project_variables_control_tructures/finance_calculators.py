#The program imports the math module for mathematical calculations. 
#Then, it displays a menu with two choices: 'investment' or 'bond'. 
#Based on the user's choice, the program asks the user for relevant inputs, 
#then performs specific calculations using those inputs. 
#Once the calculation is done, the program displays the result. 
#If the user enters an invalid input, the program prints an error message and exits.

# Importing math module for mathematical calculations
import math

#Printing a message to the user to enter their choice between investment or bond.
print("investment - to calculate the amount of interest you'll earn on your ")
print("investment bond - to calculate the amount you'll have to pay on a home loan ")
print("Enter either 'investment' or 'bond' from the menu above to proceed:")

# Getting user input for which option they would like to select and converting it to lowercase for consistency in the code.
user_choice = input().lower()


# If user selects investment
if user_choice == 'investment':
    # Get user inputs for investment calculation
    deposit_amount = float(input("Enter deposit amount: "))
    interest_rate = float(input("Enter interest rate (without a percentage sign): ")) / 100
    years = int(input("Enter investment term (in years): "))
    interest_type = input("Enter interest type (simple or compound): ").lower()
    
    # Calculate investment result based on user inputs
    if interest_type == 'simple':
        # Simple interest calculation
        interest = deposit_amount * (1 + interest_rate * years)
    elif interest_type == 'compound':
        # Compound interest calculation using math.pow() function from math module
        interest = deposit_amount * math.pow((1 + interest_rate), years)
    else:
        # If user enters invalid interest type, the program exits
        print("Invalid input for interest type.")
        exit()
    
    # Display investment result to user
    print(f"Your total investment amount after {years} years will be: £{interest:.2f}")
    
# If user selects bond
elif user_choice == 'bond':
    # Get user inputs for bond repayment calculation
    present_value = float(input("Enter present value of house: "))
    interest_rate = float(input("Enter interest rate without a percentage sign: ")) / 100 / 12
    months = int(input("Enter number of months to repay bond: "))
    
    # Calculate monthly bond repayment based on user inputs
    repayment = (interest_rate * present_value) / (1 - math.pow((1 + interest_rate), -months))
    
    # Display monthly bond repayment to user
    print(f"You will pay £{repayment:.2f} per month for the bond repayment.")
else:
    # If user enters invalid input, program prints an error message and exits.
    print("Invalid input. Please try again.")
