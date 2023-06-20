"""
Python Docstring

"""
import json
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import tflearn
import tensorflow
import random 

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs = []

for intent in data["intents"]: #  STEMMING
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)

    if intent["tag"] not in labels:
        labels.append(intent["tag"])

print("Hello")
