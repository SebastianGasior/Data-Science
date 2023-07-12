#Ask the user to input their time for each event in minutes
#Prompt the user to enter swim time in minutes
#Read and store the user input as a float variable called swim_time
#Prompt the user to enter cycle time in minutes
#Read and store the user input as a float variable called cycle_time
#Prompt the user to enter run time in minutes
#Read and store the user input as a float variable called run_time
#Calculate the total time taken to complete the triathlon
#Add the three float variables swim_time, cycle_time, and run_time together and store the result in a float variable called total_time
#Determine the award based on the total time


# Ask the user to input their time for each event in minutes
swim_time = float(input("Enter swim time (minutes): "))  # get user input for swim time and convert to float type
cycle_time = float(input("Enter cycle time (minutes): "))  # get user input for cycle time and convert to float type
run_time = float(input("Enter run time (minutes): "))  # get user input for run time and convert to float type

# Calculate the total time taken to complete the triathlon
total_time = swim_time + cycle_time + run_time  # add up the times for all three events to get the total time

# Determine the award based on the total time
if total_time <= 100:
    print("Provincial Colours")  # if the total time is less than or equal to 100, the participant earns Provincial Colours
elif total_time <= 105:
    print("Provincial Half Colours")  # if the total time is less than or equal to 105, the participant earns Provincial Half Colours
elif total_time <= 110:
    print("Provincial Scroll")  # if the total time is less than or equal to 110, the participant earns Provincial Scroll
else:
    print("No award")  # if the total time is greater than 110, the participant earns no award

