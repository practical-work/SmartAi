import pandas as pd
import joblib # or pickle
import nltk
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)

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

#print(preprocess_text("WINNER!! You have been selected to receive a $1000 prize .Claim now!"))


spam_df = pd.read_csv("LogisticRegressionModel/sms_spam.csv",encoding="latin1")
#print(spam_df.head())

spam_df["cleaned_message"] = spam_df["message"].apply(preprocess_text)

#print(spam_df["cleaned_message"].head())

# Convert text in numbers
tfidf_vectorizer = TfidfVectorizer()

# X denotes feature and y is target value for binary classification spam or ham

# separate feature and target
X = tfidf_vectorizer.fit_transform(spam_df["cleaned_message"])
y = spam_df["label"]

model = LogisticRegression()

# splitting data for training and testing purpose

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,random_state=42)
model.fit(X_train,y_train)

# print(X_train)
# print(X_test)

# for user input working
# user_input_email = input("Enter email message here : \n")

# cleaned_input = preprocess_text(user_input_email)

# input_vector = tfidf_vectorizer.transform([cleaned_input])

# pred = model.predict(input_vector)

# if pred == 0:
#    print("Ham")
# else:
#     print("Spam")

# end user input


y_pred = model.predict(X_test)

# slope and intercepts of model
print(f"Slope (b1) : {model.coef_.round(2)}")
print(f"Intercept (b0) : {model.intercept_[0]:.2f}")



# performance evaluation

accuracy = accuracy_score(y_pred,y_test)
precision = precision_score(y_pred,y_test)
recall = recall_score(y_pred,y_test)
f1 = f1_score(y_pred,y_test)
cm = confusion_matrix(y_pred,y_test)
cr = classification_report(y_pred,y_test)

print(f" Accuracy : {accuracy:.2f}")
print(f" Precision : {precision:.2f}")
print(f" Recall : {recall:.2f}")
print(f" F1 Score : {f1:.4f}")
print(f"Confusion Matrix \n {cm}")
print(f"Classification Report \n {cr}")


# Save trained model using joblib or pickle

joblib.dump(model,"LogisticRegressionModel/Logistic-reg-trained-model(for testing only ).pkl")
print("Logistic-reg-trained-model(for testing only ).pkl saved successfully !")