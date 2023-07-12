#This code uses the `Spacy` library in Python to identify named entities in a list of garden path sentences. 
#It imports the `Spacy` library, loads the English model, and processes each sentence in the list. 
#It prints the original sentence and any found named entities.

# Import spacy module
import spacy

# Load the pre-trained model 'en_core_web_sm'
nlp = spacy.load("en_core_web_sm")


# Define garden path sentences
gardenpathSentences = [
    "The old man the boat.",
    "The horse raced past the barn fell.",
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]

# Process each sentence in gardenpathSentences using the loaded model
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    # Get any named entities identified by the model in the processed sentence
    entities = doc.ents
    
    # Print the original sentence, and any named entities found in it along with their labels
    print(f"Sentence: {sentence}")
    if entities:
        for entity in entities:
            print(f"{entity.text}: {entity.label_} ({spacy.explain(entity.label_)})")
    else:
        print("No named entities found.")
        
    print()

# Print explanations for two named entity labels - GPE and ORG
print(spacy.explain("GPE"))
print(spacy.explain("ORG"))

# The entity "GPE" refers to geopolitical entities, such as countries, cities, and states.
# This entity makes sense as it can refer to a location or place associated with the sentence.

# The entity "ORG" refers to companies, institutions, or organizations.
# This entity also makes sense in terms of the sentence being related to an entity associated with an organization or company. 
