import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

word1 = nlp("car")
word2 = nlp("bicycle")
word3 = nlp("train")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens1 = nlp('car bicycle train ')
for token1 in tokens1:
    for token2 in tokens1:
        print(token1.text, token2.text, token1.similarity(token2))

'''
It is interesting to see that the similarity score between 'cat' and 'monkey' (0.56) is higher 
than the similarity score between 'banana' and 'monkey' (0.31), 
whereas 'banana' has a higher similarity score with 'cat' (0.67). 
This reveals some interesting aspects of how these words are related from a semantic point of view. 
For example, the model may be picking up on the fact that 'cat' and 'monkey' are both animals, 
while 'banana' is a fruit that is often eaten by monkeys.

An example of my own could be to compare the similarity scores between the words 
'car', 'bicycle', and 'train'. In this case, we might expect 'car' and 'train' to have a relatively high similarity 
score because they are both vehicles that travel on tracks or roads, while 'bicycle' 
would likely have a lower similarity score with either word.

When running the script with the simpler language model 'en_core_web_sm', 
one major difference noticed is that the tokens are not matched as accurately as with the 'en_core_web_md' model. 
The smaller model has a lower accuracy rate. 
This is because the 'en_core_web_sm' model is much smaller and therefore less robust 
than the larger 'en_core_web_md' model. The 'en_core_web_sm' lacks some of the features like word vectors 
which provide better semantics to understand the context of words in natural language processing. 
As a result, the similarity scores of the word pairs may be slightly different when compared to 
the 'en_core_web_md' model.
'''