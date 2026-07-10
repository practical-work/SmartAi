import pandas as pd
import joblib # or pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

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

try:
   spam_df = pd.read_csv("LogisticRegressionModel/sms_spam.csv",encoding="latin1")
except FileNotFoundError:
    print("ERR : sms_spam.csv not found.")
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
model.fit(X,y)


# Save trained model using joblib or pickle

joblib.dump(model,"LogisticRegressionModel/Logistic-reg-trained-model.pkl")
joblib.dump(tfidf_vectorizer, "LogisticRegressionModel/tfidf_vectorizer.pkl")
print("Logistic-reg-trained-model.plk and tfidf_vectorizer.pkl saved successfully !")