# Email Spam Detection using Logistic Regression

A Machine Learning web application built using **Python**, **Scikit-learn**, **Flask**, and **Natural Language Processing (NLP)** to classify SMS or email messages as **Spam** or **Not Spam (Ham)**.

This project demonstrates the complete Machine Learning workflow, from text preprocessing and feature extraction to model training, evaluation, and deployment.

---

## Project Overview

Spam messages are unwanted messages that often contain advertisements, phishing attempts, or fraudulent content.

This application predicts whether a given message is **Spam** or **Not Spam** using a Logistic Regression model trained on a real-world spam dataset.

---

## Features

- Detect Spam and Not Spam messages
- Text preprocessing using NLP techniques
- TF-IDF feature extraction
- Logistic Regression classifier
- Interactive Flask web application
- Clean and responsive user interface
- Ready for deployment on Render

---

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- NLTK
- Joblib
- HTML5
- CSS3
- Git & GitHub
- Render

---

## Project Structure

```
LogisticRegressionSpamDetection/
│
├── app.py
├── cleaning.py
├── Logistic-reg-training.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
├── spam.csv
├── trained_logistic_regression_model.pkl
├── tfidf_vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

---

## Machine Learning Workflow

### 1. Load Dataset

Load the SMS spam dataset using Pandas.

### 2. Text Preprocessing

- Convert text to lowercase
- Remove punctuation
- Remove special characters
- Remove stopwords
- Tokenization
- Stemming

### 3. Feature Extraction

Convert text into numerical features using **TF-IDF Vectorizer**.

### 4. Train-Test Split

Split the dataset into training and testing sets.

### 5. Train Logistic Regression Model

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X_train, y_train)
```

### 6. Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

### 7. Save Model

```python
import joblib

joblib.dump(model, "trained_logistic_regression_model.pkl")
joblib.dump(tfidf_vectorizer, "tfidf_vectorizer.pkl")
```

### 8. Flask Integration

The trained model predicts whether the entered message is Spam or Not Spam through a simple web interface.

---

## Installation

Clone the repository

```bash
git clone https://github.com/practical-work/SmartAi.git
```

Navigate to the project directory

```bash
cd SmartAi/LogisticRegressionSpamDetection
```

Install required packages

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Deployment

This project can be deployed on **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## Live Demo

Add your deployed Render application URL here.

```
https://logistic-regression-model.onrender.com
```

---

## Repository

https://github.com/practical-work/SmartAi/tree/main/LogisticRegressionModel

---

## Learning Outcomes

Through this project, I learned:

- Natural Language Processing (NLP) basics
- Text preprocessing
- TF-IDF Vectorizer
- Logistic Regression
- Binary Classification
- Model Evaluation
- Model Serialization using Joblib
- Flask Integration
- Machine Learning Deployment using Render
- Git & GitHub workflow

---

## Future Improvements

- Support Email (.eml) files
- Multi-language spam detection
- Deep Learning models (LSTM)
- BERT-based text classification
- Prediction history
- REST API support
- User authentication

---

## Author

**Kunal Vats**

B.Tech CSE (Artificial Intelligence & Machine Learning)

Maharshi Dayanand University (MDU), Rohtak

GitHub: https://github.com/practical-work

---

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.