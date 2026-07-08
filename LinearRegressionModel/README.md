# Student Performance Prediction using Linear Regression

A Machine Learning web application built with **Python**, **Scikit-learn**, and **Flask** to predict student performance based on various academic and personal factors. This project demonstrates the complete Machine Learning workflow, from data preprocessing and model training to deployment as a web application.

---

## Project Overview

This project uses the **Linear Regression** algorithm to predict a student's performance using input features such as study hours, attendance, previous scores, and other relevant attributes.

The application includes:

- Data preprocessing
- Feature encoding and scaling (if required)
- Model training using Scikit-learn
- Model serialization using Joblib
- Prediction through a Flask web interface
- Ready for deployment on Render

---

## Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3

---

## Project Structure

```
LinearRegressionModel/
│
├── app.py                     # Flask Application
├── trained_model.pkl          # Saved Machine Learning Model
├── Student_Performance_Data.csv
├── student_performance.csv
├── PreprocessedData.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

---

## Machine Learning Workflow

### Step 1 - Load Dataset

- Read the dataset using Pandas.

### Step 2 - Data Preprocessing

- Handle missing values
- Encode categorical variables
- Select features
- Split dataset into training and testing data

### Step 3 - Train Model

Train a Linear Regression model using Scikit-learn.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
```

---

### Step 4 - Evaluate Model

Evaluate using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

### Step 5 - Save Model

```python
import joblib

joblib.dump(model, "trained_model.pkl")
```

---

### Step 6 - Deploy with Flask

Users enter the required details through the web interface, and the Flask backend loads the trained model to generate predictions.

---

## Installation

Clone the repository.

```bash
git clone https://github.com/practical-work/SmartAi.git
```

Move to the project directory.

```bash
cd SmartAi/LinearRegressionModel
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the Flask application.

```bash
python app.py
```

Open your browser.

```
http://127.0.0.1:5000
```

---

## Deployment

This project is configured to be deployed on **Render**.

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
gunicorn app:app
```

---

## Features

- Clean and responsive user interface
- Predict student performance instantly
- Trained Linear Regression model
- Easy deployment using Render
- Beginner-friendly project structure
- Well-organized codebase

---

## Future Improvements

- Add Multiple Regression models
- Compare different ML algorithms
- Model performance visualization
- Database integration
- User authentication
- Prediction history
- REST API support

---

## Learning Objectives

Through this project, you will understand:

- Data preprocessing
- Feature engineering
- Train-test split
- Linear Regression
- Model evaluation
- Saving and loading ML models
- Flask integration
- Machine Learning deployment

---

## Author

**Kunal Vats**

B.Tech CSE (Artificial Intelligence & Machine Learning)

Maharshi Dayanand University (MDU), Rohtak

GitHub: https://github.com/practical-work

---

## Repository

https://github.com/practical-work/SmartAi

---

## License

This project is created for educational and learning purposes.