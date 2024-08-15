import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')


def lowercase(text):
    return text.lower()


def punctuation_removal(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def tokenize(text):
    return nltk.word_tokenize(text)


def remove_stopwords(tokens):
    stop_words = nltk.corpus.stopwords.words('english')
    return [token for token in tokens if token not in stop_words]


def stemming(tokens):
    stemmer = nltk.PorterStemmer()
    return [stemmer.stem(token) for token in tokens]


def preprocess_text(text):
    text = lowercase(text)
    text = punctuation_removal(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stemming(tokens)
    return tokens