#Set sentence variable to "The!quick!brown!fox!jumps!over!the!lazy!dog!"
#Replace all "!" in sentence with a blank using the replace() function and store the new sentence in replaced_sentence variable
#Print replaced_sentence
#Convert replaced_sentence to uppercase using the upper() function and store the new sentence in uppercase_sentence variable
#Print uppercase_sentence
#Reverse uppercase_sentence and store the reversed sentence in reverse_sentence variable
#Print reverse_sentence



# Save the sentence as a single string
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!"

# Replace every "!" exclamation mark with a blank space
sentence_replaced = sentence.replace("!", " ") # Replacing all "!" with blank spaces
print(sentence_replaced) # Printing the replaced sentence

# Print the sentence in uppercase
sentence_uppercase = sentence_replaced.upper() # Converting the sentence to uppercase
print(sentence_uppercase) # Printing the uppercase sentence

# Print the sentence in reverse
sentence_reverse = sentence_uppercase[::-1] # Reversing the uppercase sentence
print(sentence_reverse) # Printing the reversed sentence