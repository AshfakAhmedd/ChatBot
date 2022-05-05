import numpy as np
import nltk

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):

    return nltk.word_tokenize(sentence)


def stem(word):

    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, word in enumerate(words):
        if word in sentence_words:
            bag[idx] = 1

    return bag