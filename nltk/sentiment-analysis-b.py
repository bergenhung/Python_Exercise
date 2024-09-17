import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download()

messages = {
    'I love this poduct!',
    'Your company is terrible',
    'It\'s totally inconsiderate to make people wait like this',
    'I can\'t believe I\'ve had to wait this long!',
    'I ate a sandwich',
}

sia = SentimentIntensityAnalyzer()

scores = []

for m in messages:
    scores.append({'messages': m, 'scores': sia.polarity_scores(m)})

print(scores)