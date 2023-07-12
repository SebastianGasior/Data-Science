#code initiates two variables, "num_sum" and "count", to store the sum and count of entered numbers, respectively. 
#It proceeds to prompt the user to input a number and continues to do so until "-1" is entered. 
#Within the while loop, each entered number is added to the sum, and the count of entered numbers is incremented accordingly. 
#Following the while loop, we verify if any numbers were entered (i.e., the count is non-zero), 
#and calculate the average by dividing the sum by the count.
#It prints the average value, rounded to 2 decimal places, using f-strings.


# Initialize variables to hold the sum and count of numbers entered
num_sum = 0
count = 0

# Ask user to enter a number
num = int(input("Enter a number (-1 to stop): "))

# Keep asking for numbers until -1 is entered
while num != -1:
    # Add the number to the sum
    num_sum += num
    
    # Increment the count of numbers entered
    count += 1
    
    # Ask for another number
    num = int(input("Enter a number (-1 to stop): "))
    
# Calculate the average, excluding -1
if count == 0:
    print("No numbers were entered.")
else:
    avg = num_sum / count
    print(f"The average of the {count} numbers entered is: {avg:.2f}")
