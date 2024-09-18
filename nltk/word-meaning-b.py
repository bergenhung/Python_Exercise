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
    if meaning:
        print(f'{word}: {[defis.definition() for defis in meaning]}')
        print(f'Synonyms:, {[lemma.name() for lemma in meaning[0].lemmas()]}')
        print(f'Antonyms:, {[anton.name() for lemma in meaning[0].lemmas() for anton in lemma.antonyms()]}\n')
