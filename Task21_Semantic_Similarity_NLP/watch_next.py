'''

This program utilizes a pre-trained spaCy model designed for the English language. 
Its purpose is to identify the movie title that bears the closest resemblance to a given movie description 
within a provided list. The program encompasses a function called find_similar_movie() which accepts an input 
description. It proceeds to read a file containing multiple movie descriptions, 
leveraging the spaCy model to calculate the similarity score between the input description and each movie 
description. Ultimately, it returns the most similar movie title as a list, consisting of a single string element.

In addition, the program features an instance of a movie description (description). 
It invokes the find_similar_movie() function, passing this description as an argument. 
Subsequently, it prints the resulting list, containing the most similar movie title, to the terminal.
'''

import spacy

# Load the pre-trained spaCy model for English
nlp = spacy.load("en_core_web_md")

# Define the path to the file containing the list of movie descriptions
movies_file = "C:/Hyperion Dev/Data Science/Task21_Semantic_Similarity_NLP/movies.txt"

# Define a function to find the most similar movie title for a given description
def find_similar_movie(description):
    # Open the file containing the list of movie descriptions
    with open(movies_file, 'r') as f:
        # Read the contents of the file into a list of strings (one per line)
        movie_descriptions = f.read().splitlines()

    # Convert the input description into an nlp object using the spaCy model
    model_description = nlp(description)
    
    # Create an empty list to store the similarity scores between the input description and each movie description
    similarity_scores = []
  
    # Iterate over the list of movie descriptions
    for movie in movie_descriptions:
        # Convert the current movie description into an nlp object using the spaCy model
        nlp_movie = nlp(movie)
        
        # Compute the similarity score between the input description and the current movie description
        similarity_score = model_description.similarity(nlp_movie)
        
        # Append the similarity score to the list of similarity scores
        similarity_scores.append(similarity_score)

    # Find the index of the movie with the highest similarity score
    most_similar_idx = similarity_scores.index(max(similarity_scores))
    
    # Return the most similar movie title as a list containing a single string element
    return [movie_descriptions[most_similar_idx]]

# Define an example movie description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Call the find_similar_movie function with the example movie description
most_similar_movie = find_similar_movie(description)

# Print the most similar movie title as a list
print(f"The most similar movie title is: {most_similar_movie}")
