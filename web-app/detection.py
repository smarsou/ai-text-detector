import time
import pickle
import numpy
import fasttext
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('all')
embedding_model = fasttext.load_model('model/fasttext.bin')
lemmatizer = WordNetLemmatizer()
with open('model/random_forest_bigdataset.pkl', 'rb') as file:
    best_model = pickle.load(file)

def clean(prompt):
    r = re.sub('[^a-zA-Z]', ' ', str(prompt))
    r = r.lower()
    r = r.split()
    ## we can also tokenize with nltk.tokenize et word_tokenization()
    r = [word for word in r if word not in stopwords.words('english')]
    r = [lemmatizer.lemmatize(word) for word in r]
    r = ' '.join(r)
    return r

def get_vect(word):
    try:
      return embedding_model.get_word_vector(word)
    except KeyError:
        return numpy.zeros((embedding_model.vector_size,))

def sum_vectors(phrase):
    return sum(get_vect(w) for w in phrase)/len(phrase)

def features(X):
    feats = numpy.vstack([sum_vectors(p) for p in X])
    return feats

def detect_ai(prompt):
  new_prompt = clean(prompt)
  X = sum_vectors(new_prompt).reshape(1,-1)
  proba = best_model.predict_proba(X)
  print(proba)
  return int(proba[0][0]*100)
