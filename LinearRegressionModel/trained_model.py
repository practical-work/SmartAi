import pandas as pd
#import numpy as np
import joblib # or pickle 
#import pickle
#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
#from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
#from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder,OneHotEncoder


# Reading cleaned csv file 
try:
   student_df = pd.read_csv("LinearRegressionModel/Student_Performance_Data.csv",encoding="utf-8")
   print("Data Loaded successfully .")
except FileNotFoundError:
   print("Error: 'LinearRegressionModel/Student_Performance_Data.csv' was not found.")
   exit()

# print(student_df.head(3))

# No need for label and one hot encoding beco'z no categorical values present in dataset

# Separate the features (X) and target or predicted value (y)
X = student_df[["Study_Hours","Attendance_Percentage","Previous_Exam_Score","Assignment_Completion"]]  # Multiple value Linear Regression 
y = student_df["Final_Exam_Score"]

# No feature scaling is required.

# Create & train model 
model = LinearRegression()  
model.fit(X,y)  # input-output already mapped means known
print("Model trained successfully !")

# Use joblib/pickle to save this trained model file with .pkl
joblib.dump(model,"LinearRegressionModel/student_performance_model_01.pkl")
print("student_performance_model_01  saved successfully.")