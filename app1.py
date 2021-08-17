# -*- coding: utf-8 -*-
"""app_nlp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12Et6-yqsVSoXBu5zDfnTVxw7J-I8zk0h
"""

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from sklearn.preprocessing import LabelBinarizer
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import feature_extraction, linear_model, model_selection, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import MultinomialNB

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.gaussian_process import GaussianProcessClassifier
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping
import string
from nltk.stem import WordNetLemmatizer 
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report

app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])

def predict()
    fakenews = pd.read_csv("Fake.csv")
    realnews = pd.read_csv("True.csv")

    news=pd.concat([realnews,fakenews])

    lm = WordNetLemmatizer() 
    def clean_text(words):
  
        words=re.sub('[^a-zA-Z]',' ',words)
        words=words.lower()
        words=words.split()
        words=[lm.lemmatize(word) for word in words]
        words=' '.join(words)
        return words
      
    news['text']=news['text'].apply(clean_text)
    x_train,x_test,y_train,y_test = train_test_split(news['text'],news.category, test_size=0.1, random_state=2020)
    pipe = Pipeline([('vect', CountVectorizer()),
                 ('tfidf', TfidfTransformer()),
                 ('model', XGBClassifier(loss = 'deviance',
                                                   learning_rate = 0.01,
                                                   n_estimators = 10,
                                                   max_depth = 5,
                                                   random_state=2020))])

    model = pipe.fit(x_train, y_train)
    prediction = model.predict(x_test)
    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        my_prediction = model.predict(vect)
        return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
  app.run(debug=True)

