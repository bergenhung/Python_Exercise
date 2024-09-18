import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

messages = {
    'I love this poduct!',
    'Your company is terrible. I can\'t believe I\'ve had to wait this long!',
    'It\'s totally inconsiderate to make people wait like this.',
    'I ate a sandwich.',
}
demowords = ['playing', 'happiness', 'going', 'doing', 'do', 'yes', 'no', 'I', 'having', 'had', 'haved', 'coding', 'programming', 'code', 'program']

lematizer = WordNetLemmatizer()
stemmer = PorterStemmer()
for word in demowords:
    print(word, stemmer.stem(word),lematizer.lemmatize(word,"v"))

sia = SentimentIntensityAnalyzer()
for sentence in messages:
    token_words = []
    sentence_no_stopwords = []
    print(f'{sentence:} \n {sia.polarity_scores(sentence)}')
    token_words.extend(word_tokenize(sentence))
    sentence_no_stopwords = [word for word in token_words if word not in stop_words]
    print(f'{' '.join(sentence_no_stopwords):} \n {sia.polarity_scores(' '.join(sentence_no_stopwords))}')
