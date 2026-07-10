import pandas as pd
import numpy as np
import joblib # or pickle
from flask import Flask,render_template,redirect,request,url_for
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)
import nltk
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))
#print(stop_words)

# creating function for text preprocessing

def preprocess_text(text):
    #lowercasing
    text = text.lower()
    # remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    # tokenization
    tokens = nltk.word_tokenize(text)
    # stemming and remove stopwords
    cleaned_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]

    return " ".join(cleaned_tokens)


app = Flask(__name__) # Web or Flask Application

# load trained model
try:
    with open("Logistic-reg-trained-model.pkl","rb") as file:
        model = joblib.load(file)
        print("Successfully load trained model.")
except Exception as e:
    print(e)
    exit()

# load tf-idf Vectorizer
try:
    with open("tfidf_vectorizer.pkl","rb") as file2:
        tfidf_vectorizer = joblib.load(file2)
        print("Successfully load tfidfvectorizer.")
except Exception as e:
    print(e)
    exit()

# read csv file
try:
    spam_df = pd.read_csv("sms_spam.csv",encoding="latin1")
    print("sms_spam.csv loaded successfully.")
except Exception as e:
    print(e)


spam_df["cleaned_message"] = spam_df["message"].apply(preprocess_text)

X = tfidf_vectorizer.transform(spam_df["cleaned_message"])

y = spam_df["label"]

y_pred = model.predict(X)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Classification",methods=["POST"])
def Classification():
    if (request.method == "POST"):
        user_input = request.form.get("msg")
        cleaned_input = preprocess_text(user_input)
        input_vector = tfidf_vectorizer.transform([cleaned_input])
        prediction = model.predict(input_vector)[0]
        
        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(y, y_pred)
        recall = recall_score(y, y_pred)
        f1 = f1_score(y, y_pred)
        cm = confusion_matrix(y, y_pred)
        cr = classification_report(y, y_pred)


    return render_template("index.html",prediction=prediction,intercept=f"{model.intercept_[0]:.2f}",coefs=f"{model.coef_.round(2)}"
                           ,accuracy=f"{accuracy:.2f}",precision=f"{precision:.2f}",recall=f"{recall:.2f}",f1=f"{f1:.4f}",cm=cm,cr=cr)


if __name__ == "__main__":
    app.run(debug=True)