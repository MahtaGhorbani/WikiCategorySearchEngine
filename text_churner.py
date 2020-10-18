import string
import numpy as np
import math
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def get_keywords(text):
    text.rstrip()

    """
    Remove stop words and punctuation
    """
    stop_words = stopwords.words('english') + list(string.punctuation)
    text = ' '.join([
        word for word in text.split()
        if word.lower() not in stop_words
    ])

    tokens = nltk.word_tokenize(text)
    return tokens

