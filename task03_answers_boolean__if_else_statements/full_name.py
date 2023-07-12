#Ask the user to enter their full name
#Check if the length of the user's input is less than 4 characters or more than 25 characters
#If the length of the input is less than 4, display the message "You have entered less than 4 characters. Please make sure that you have entered your name and surname."
#If the length of the input is more than 25, display the message "You have entered more than 25 characters. Please make sure that you have only entered your full name."
#If the length of the input is between 4 and 25 characters, continue to the next step
#Check if the user's input contains at least one space character (to separate their first and last name)
#If the input does not contain a space character, display the message "You haven’t entered anything. Please enter your full name."
#If the input contains a space character, continue to the next step
#Display the message "Thank you for entering your name." 




# Asks user to input their full name and assigns it to variable 'name'
name = input("Please enter your full name: ")

# Checks if the length of 'name' string is 0, meaning that nothing was inputted
if len(name) == 0:
  print("You haven't entered anything. Please enter your full name.")
  
# Checks if the length of 'name' string is less than 4 characters
elif len(name) < 4:
  print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
  
# Checks if the length of 'name' string is more than 25 characters
elif len(name) > 25:
  print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
  
# If none of the above conditions are met, prints a thank you message for entering name
else:
  print("Thank you for entering your name.")