import time
import pickle
import numpy
import fasttext
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
embedding_model = fasttext.load_model('model/fasttext.bin')
with open('model/random_forest_bigdataset.pkl', 'rb') as fichier:
    best_model = pickle.load(fichier)
lemmatizer = WordNetLemmatizer()