raw_email = "WINNER!! You have been selected to receive a $1000 prize.Claim now!"

# Learning test preprocessing because Computers only understand numericals values not string or categorical data

#1. lowercasing
lowercased_email = raw_email.lower()
#print(lowercased_email)

#2. Remove punctuation like !@& etc.
import string

#print(string.punctuation)
email_no_punctuation = "".join([char  for char in lowercased_email if char not in string.punctuation])
#print(email_no_punctuation)

#3. Tokenization (Breaking into smaller tokens (words))
import nltk
nltk.download('punkt_tab',quiet=True) # use nltk.download('punkt') standard 
from nltk.tokenize import word_tokenize

email_tokens = word_tokenize(email_no_punctuation)
#print(email_tokens)


#4. Removal of Stop Words like is,you,the,a etc. 
nltk.download('stopwords',quiet=True)

from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
#print(stop_words)

email_no_stopwords = [word for word in email_tokens if word not in stop_words]
#print(email_no_stopwords)


#5. Stemming or Lemmatization
from nltk.stem import PorterStemmer,WordNetLemmatizer
nltk.download('wordnet',quiet=True)

stemmer = PorterStemmer()
          #OR
Lemmatizer = WordNetLemmatizer()

email_with_stemming = [stemmer.stem(word) for word in email_no_stopwords]
#print(email_with_stemming)
             #OR
email_with_lemmatization = [Lemmatizer.lemmatize(word) for word in email_no_stopwords]
#print(email_with_lemmatization)

# 6. Vectorization phase (Covert text into numbers)

# Re Join cleaned tokens into united string
cleaned_email = " ".join(email_with_stemming)
#print(type(cleaned_email))

from sklearn.feature_extraction.text import CountVectorizer

bow_vectorizer = CountVectorizer()

bow_matrix = bow_vectorizer.fit_transform([cleaned_email])

#print("Vocabulary",bow_vectorizer.get_feature_names_out())
#print("BOW matrix \n",bow_matrix.toarray())


             # OR

# TF-IDF vectorization

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix = tfidf_vectorizer.fit_transform([cleaned_email])

# print("Vocabulary",tfidf_vectorizer.get_feature_names_out())
# print("BOW matrix \n",tfidf_matrix.toarray())
