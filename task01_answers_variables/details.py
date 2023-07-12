# Prompt the user to input their name, age, house number, and street name.
# Store the user's name in a variable.
# Store the user's age in a variable.
# Store the user's house number in a variable.
# Store the user's street name in a variable.
# Print out a single sentence containing all the details of the user
# (name, age, house number, street name)
name = input("What is your name? ")
age = int(input("How old are you? "))
house_number = int(input("What is your house number? "))
street_name = input("What is your street name? ")

# Print out a single sentence containing all the details of the user
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name} Street.")