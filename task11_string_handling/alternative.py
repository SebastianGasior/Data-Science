#The code defines a function named alternate_string that takes a string and returns a modified version of it. 
#It creates an empty string called new_string and loops through each character of the input string using the 
#range function. If the index of the current character is even, it converts that character to uppercase 
#and appends it to the new string; if it's odd, it converts the character to lowercase and appends it to the new string. 
#It then returns the new modified string.

# Define a function called `alternate_string` that takes a string as input.
def alternate_string(string):
    # Create an empty string variable called `new_string`.
    new_string = ""

    # Loop over each character in the original input string using its index `i`.
    for i in range(len(string)):
        # Use an if statement to check if the current index `i` is even.
        if i % 2 == 0:
            # If even, append the uppercase version of the character to `new_string`.
            new_string += string[i].upper()
        else:
            # If odd, append the lowercase version of the character to `new_string`.
            new_string += string[i].lower()

    # Return the modified string (a new string containing every other letter in alternating case).
    return new_string

# Prompt user to enter a string value and assign it to a variable.
input_string = input("Enter a string: ")

# Call the `alternate_string` function with the user-entered string as its argument.
# Print the output of the function (a modified version of the original string) to screen. 
print(alternate_string(input_string))

#The code defines a function named alternate_words that accepts a string as input. 
#It converts the input string into a list of individual words using the split() method. 
#It then iterates through each word in the list using a for loop and an index i. 
#If i is even, it converts the current word to lowercase and replaces it back in the original list; if i is odd, 
#it converts the current word to uppercase and replaces it back in the original list. 
#Then it uses the join() method to create a modified string by joining all the altered words with a space. 
#The code prompts the user to enter a string and stores it in a variable called input_string. 
#Finally, it displays the modified string by calling the alternate_words function and passing input_string as an argument. 
#The modified string has every alternate word in uppercase and all remaining words in lowercase.


# Define a function called alternate_words that takes a string as input.
def alternate_words(string):
    # Convert input string into a list of individual words, and store in variable `words`.
    words = string.split()

    # Loop over every word in the list, using an index `i`. 
    for i in range(len(words)):
        # Use an if statement to check if the current index `i` is even. 
        if i % 2 == 0:
            # If even, convert the word to lowercase using the `lower()` method and replace it in the original list.
            words[i] = words[i].lower()
        else:
            # If odd, convert the word to uppercase using the `upper()` method and replace it in the original list. 
            words[i] = words[i].upper()

    # Join every word in the list back into a single string, separated by spaces.
    # Return this modified string as the function output.
    return " ".join(words)

# Prompt user to enter a string value and assign it to a variable.
input_string = input("Enter a string: ")

# Call the `alternate_words` function with the user-entered string as its argument.
# Print the output of the function (a modified version of the original string) to screen. 
print(alternate_words(input_string))

