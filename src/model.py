from __future__ import annotations
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

def build_model(ngram_range=(1,2), min_df=2):
    return Pipeline([('tfidf',TfidfVectorizer(ngram_range=ngram_range,min_df=min_df,sublinear_tf=True,max_features=50000)),('clf',LogisticRegression(max_iter=2000,class_weight='balanced'))])

def evaluate(model,X_test,y_test):
    return classification_report(y_test,model.predict(X_test),output_dict=True,zero_division=0)
