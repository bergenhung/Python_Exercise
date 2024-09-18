import nltk

# nltk.download()
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

messages = {
    'I love this poduct!',
    'Your company is terrible. I can\'t believe I\'ve had to wait this long!',
    'It\'s totally inconsiderate to make people wait like this.',
    'I ate a sandwich.',
}

print(stop_words)

token_words = []
token_wo_stopwords = []
for sentence in messages:
    token_words.extend(word_tokenize(sentence))
print(f'\n{token_words}\n')

for word in token_words:
    if word not in stop_words:
        token_wo_stopwords.append (word)
# token_wo_stopwords_tuples = tuple(token_wo_stopwords)
print(token_wo_stopwords)
print(f'\n{set(token_words)-set(token_wo_stopwords)}')
