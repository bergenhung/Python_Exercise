import nltk
import matplotlib.pyplot as plt

# nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words ('english'))

messages = {
    'I love this poduct!',
    'Your company is terrible. I can\'t believe I\'ve had to wait this long!',
    'It\'s totally inconsiderate to make people wait like this.',
    'I ate a sandwich.',
}

print (stop_words)
token_words = []
for sentence in messages:
    token_words.extend(word_tokenize(sentence))
print (token_words)
token_tuples = tuple(token_words)
print (token_tuples)
