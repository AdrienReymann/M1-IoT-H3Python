import pandas as pd
import re
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from stop_words import get_stop_words
from flask import Flask

tweet = pd.read_csv("labels.csv",sep=",")
tweet.rename(columns={'Unnamed: 0': 'id'}, inplace=True)

app = Flask(__name__)

@app.route('/')
def home():
    return tweet.head(5)

if __name__ == "__main__":
   app.run()


tweet['tweet'] = tweet['tweet'].apply(lambda tweet: re.sub('[^A-Za-z]+', ' ', tweet.lower()))
tweet.head(5)
clf = sklearn.pipeline.make_pipeline(
    TfidfVectorizer(stop_words=get_stop_words('en')),
    OneVsRestClassifier(SVC(kernel='linear', probability=True))
)