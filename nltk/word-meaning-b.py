import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import wordnet
from itertools import chain

messages = {
    'I love this poduct!',
    'Your company is terrible. I can\'t believe I\'ve had to wait this long!',
    'It\'s totally inconsiderate to make people wait like this.',
    'I ate a sandwich.',
}

token_words = list(chain.from_iterable([word_tokenize(sentence) for sentence in messages]))

for word in token_words:
    meaning = wordnet.synsets(word)
    if len(meaning) > 0:
        print(f'{word}: {meaning[0].definition()}')
