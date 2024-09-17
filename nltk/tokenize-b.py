import nltk
import matplotlib.pyplot as plt

# nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist

messages = {
    'I love this poduct!',
    'Your company is terrible. I can\'t believe I\'ve had to wait this long!',
    'It\'s totally inconsiderate to make people wait like this.',
    'I ate a sandwich.',
}

token_words = []
for sentence in messages:
    token_words.extend(word_tokenize(sentence))
print (token_words)
token_tuples = tuple(token_words)
print (token_tuples)

token_sentence = []
for sentence in messages:
    token_sentence.append({'messages:': sentence, 'tokens:': sent_tokenize(sentence)})
print (token_sentence)

fd = FreqDist(token_tuples)
print (fd.most_common(3))
fd.plot(30, cumulative=False)
plt.show()
