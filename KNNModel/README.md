# Titanic Survival Prediction using K-Nearest Neighbors (KNN)

A Machine Learning classification project built using **Python**, **Scikit-learn**, **Pandas**, **Flask**, **HTML**, **CSS**, and **JavaScript**.

This project predicts whether a passenger would survive the Titanic disaster based on passenger information using the K-Nearest Neighbors (KNN) classification algorithm.

---

## Features

- Data preprocessing
- Missing value handling
- Exploratory Data Analysis (EDA)
- Label Encoding
- One-Hot Encoding
- Feature Scaling using StandardScaler
- KNN Classification Model
- Model Evaluation
- Model Serialization using Joblib
- Flask Web Application
- Clean and responsive user interface

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- HTML5
- CSS3
- JavaScript
- Joblib

---

## Machine Learning Workflow

1. Load Titanic Dataset
2. Clean Dataset
3. Handle Missing Values
4. Remove Unnecessary Columns
5. Perform Exploratory Data Analysis
6. Split Features and Target
7. Encode Categorical Features
8. Apply Feature Scaling
9. Train KNN Classifier
10. Evaluate Model Performance
11. Save Trained Model
12. Deploy using Flask

---

## Dataset Features

| Feature | Description |
|----------|-------------|
| Pclass | Passenger Class |
| Sex | Gender |
| Age | Passenger Age |
| SibSp | Number of Siblings/Spouses |
| Parch | Number of Parents/Children |
| Fare | Ticket Fare |
| Embarked | Port of Embarkation |

Target Variable

- Survived

---

## Project Structure

```
KNNModel/
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   └── index.html
│
├── app.py
├── train.csv
├── cleaned_titanic.csv
├── dataprocess.py
├── knn_model_training_testing.py
├── knn_trained_model.pkl
├── label_encoder.pkl
├── standard_scaler.pkl
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 83% |
| Precision | 82% |
| Recall | 76% |
| F1 Score | 78.87% |

---

## Installation

Clone the repository

```bash
git clone https://github.com/practical-work/SmartAi.git
```

Navigate to the project directory

```bash
cd KNNModel
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Learning Outcomes

This project demonstrates practical implementation of:

- K-Nearest Neighbors (KNN)
- Classification Problems
- Data Cleaning
- Missing Value Handling
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Model Evaluation
- Machine Learning Deployment using Flask

---

## Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross Validation
- Interactive data visualizations
- Model comparison with other classification algorithms
- Responsive dashboard
- Cloud deployment

---

## Author

Kunal Vats

B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)

Maharshi Dayanand University, Rohtak

---

## License

This project is licensed under the MIT License.