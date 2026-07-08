import pandas as pd
import numpy as np
import joblib # or pickle 
#import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
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
y = student_df["Final_Exam_Score"]  # [[]] means for dataframe and [] for series

# split data into train and test data's

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# print(X_train)

# print(X_test)

# No feature scaling is required.

# Create & train model 
model = LinearRegression()  
model.fit(X_train,y_train)  # input-output already mapped means known

# Make Predictions
pred_y = model.predict(X_test)

# To know value of Slope (coef_:0.2f) and Intercept (intercept_:0.2f)  y = m * X + c
# print(f"Slope (b1,b2,b3,b4) : {model.coef_.round(2)}")
print("\nSlope (Coefficient) Values")
# for feature,coef in zip(X.columns,model.coef_):
#    print(f"{feature} : {round(coef,2)}")
for feature,coef in zip(X.columns,model.coef_):
   print(f"{feature:<25}:{coef:.2f}")
#
# y = b0 +b1*X1+b2*X2+b3*X3+b4*X4
print(f"Intercept (b0) : {model.intercept_:.2f}")

# Performance measure parameters
mae = mean_absolute_error(y_test,pred_y)
mse = mean_squared_error(y_test,pred_y)
rms = np.sqrt(mse)
r2 = r2_score(y_test,pred_y)


print(f"Mean Absolute Error : {mae:.2f}")
print(f"Mean Squared Error : {mse:.2f}")
print(f"Root Mean Squared Error : {rms:.2f}")
print(f"R2 Score : {r2:.4f}")


# Use joblib/pickle to save this trained model file with .pkl and load any time in python file

# with open("student_performance_model.pkl","wb")as file:
#    pickle.dump(model,file)
#    print("student_performance_model File save successfully.")

joblib.dump(model,"LinearRegressionModel/student_performance_model.pkl")
print("student_performance_model  saved successfully.")