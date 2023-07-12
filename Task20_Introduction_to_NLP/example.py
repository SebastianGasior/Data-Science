# ------------------------- spaCy -------------------------------------
# spaCy is a Python natural language processing library specifically designed with
# the goal of being a useful library for implementing production-ready systems.
# It is particularly fast and intuitive, making it a top contender for NLP tasks.

# ------------------------- IMPORTANT -------------------------------------
#	Please make sure you have read and understand the instructions for this task.
#	We will be working with the *spaCy* which is an EXTERNAL Python module.
#	YOU MUST INSTALL IT BEFORE YOU CAN COMPLETE THIS TASK. 

# ************************** INSTALLATION **************************************
# Before doing anything, you need to have spaCy installed, as well as its English language model.

# Type the following commands in command line
# pip3 install spacy
# python3 -m spacy download en_core_web_sm  
# ----------------OR----------------------
# pip install spacy
# python -m spacy download en_core_web_sm

# ======= Working with the spaCy ===== #

import spacy #This statement should work if you have spaCy installed 

nlp = spacy.load('en_core_web_sm')

sample = u"Build your data science skills to launch an in-demand, valuable career in six months."

doc = nlp(sample)

# Tokenisation------------------------------------------------------------------

# Tokenisation is a foundational step in many NLP tasks. Tokenising text is the
# process of splitting a piece of text into words, symbols, punctuation, spaces,
# and other elements, thereby creating “tokens”. A naive way to do this is to
# simply split the string on white space:
doc.text.split()

'''Output: ['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in-demand,'
, 'valuable', 'career', 'in', 'six', 'months.']'''

# On the surface, this looks fine. But, note that a) it disregards the punctuation and
# Put differently, it is naive, it fails to recognise elements of the text that help
# us (and a machine) to understand its structure and meaning. Let’s see how spaCy handles this:
[token.orth_ for token in doc]

''' Output: 
['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', '-',
'demand', ',', 'valuable', 'career', 'in', 'six', 'months', '.'] '''

# Here we access the each token’s .orth_ method, which returns a string representation
# of the token rather than a spaCy token object, this might not always be desirable,
# but worth noting. SpaCy recognises punctuation and is able to split these punctuation
# tokens from word tokens. Many of spaCy’s token methods offer both string and integer
# representations of processed text – methods with an underscore suffix return strings,
# methods without an underscore suffix return integers. For example:
print([(token, token.orth_, token.orth) for token in doc])

'''
Output: 
[(Build, 'Build', 5389077834083678306),
(your, 'your', 1572612192562026184),
(data, 'data', 6645506661261177361), ]
...
'''
# If you want to avoid returning tokens that are punctuations or white space, spaCy
# provides convenient methods for this

print([token.orth_ for token in doc if not token.is_punct | token.is_space])

'''Output:
['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', 'demand',
 'valuable', 'career', 'in', 'six', 'months']
'''

# Let's identify stop words. We imported the word list above, so it's just a
# matter of iterating through the tokens stored in the Doc object and performing
# a comparison:

for word in doc:
    if word.is_stop == True:
        print(word)
'''
Output:
your
to
an
in
in
six   '''


# Lemmatisation -------------------------------------------------------------

# A related task to tokenisation is lemmatisation. Lemmatisation is the process
# of reducing a word to its base form, its mother word if you like. Different
# uses of a word often have the same root meaning. For example, practise, practised
# and practising all essentially refer to the same thing. It is often desirable
# to standardise words with similar meaning to their base form. With spaCy we can
# access each word’s base form with a token’s .lemma_ method:

sing = "sang singing sing"
nlp_practice = nlp(sing)
print([word.lemma_ for word in nlp_practice])

'''Output: ['sing', 'singe', 'sing'] '''

# Why is this useful? An immediate use case is in machine learning, specifically
# text classification. Lemmatising the text prior to, for example, creating a
# “bag-of-words” avoids word duplication and, therefore, allows for the model to
# build a clearer picture of patterns of word usage across multiple documents.


# Named entity recognition

# Named entity recognition is the process of classifying named entities found in a text
# into pre-defined categories, such as persons, places, organisations, dates,
# etc. spaCy uses a statistical model to classify a broad range of entities,
# including persons, events, works-of-art and nationalities / religions (see the
# documentation for more information https://spacy.io/usage/linguistic-features#named-entities).

# For example, let’s take the first two sentences from Priyanka Chopra's wikipedia
# entry. We will parse this text, then access the identified entities using the
# doc object’s .ents method. With this method called on the doc we can access
# additional token methods, specifically .label_ and .label:

wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

# Get labels and entities and print them
nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

'''Output:
 [(Priyanka Chopra Jonas, 'PERSON', 378), (Indian, 'NORP', 379), (
, 'GPE', 382), (2000, 'CARDINAL', 394), (
, 'GPE', 382), (One, 'CARDINAL', 394), (India, 'GPE', 382), (Chopra, 'ORG', 381), (
, 'GPE', 382), (a National Film Award, 'EVENT', 385), (five, 'CARDINAL', 394),
(Filmfare Awards, 'FAC', 9191306739292312949), (2016, 'DATE', 388), (the Government
, 'ORG', 381), (India, 'GPE', 382), (Padma Shri, 'PERSON', 378), (Time, 'ORG', 381),
(one, 'CARDINAL', 394), (100, 'CARDINAL', 394)]'''

# Get an explanation of an entity and print it
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")
