from flask import Flask,render_template,request,url_for,flash,redirect
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import pandas as pd
import numpy as np
import matplotlib    # no new window open for plots working/processing in background
matplotlib.use('agg')
import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns
import joblib  # or pickle for loading trained model file with .pkl extension


app = Flask(__name__) # web/flask  application

# Reading trained model file with .pkl extension
try:
    with open("student_performance_model_01.pkl","rb") as file:
        model = joblib.load(file)
except Exception as e:
    print(e)
    exit()


# Read actual data from LinearRegressionModel/Student_Performance_Data.csv file for plotting using matplotlib
# Reading cleaned csv file 
try:
   student_df = pd.read_csv("Student_Performance_Data.csv",encoding="utf-8")
   print("Data Loaded successfully .")
except FileNotFoundError:
   print("Error: 'Student_Performance_Data.csv' was not found.")
   exit()

X = student_df[["Study_Hours","Attendance_Percentage","Previous_Exam_Score","Assignment_Completion"]]  # Multiple value Linear Regression 
y = student_df["Final_Exam_Score"]


# App Routing
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["GET","POST"])
def predict():
    predicted_value = None
    plot_url = None
    mse = mae = rmse = r2 = None
    if(request.method == "POST"):
      try:
        for i in X.columns:
          if(request.form.get(i) == ""):
             return render_template("index.html",predicted_value=f"{i} is required.")
            
        Study_Hours_value = request.form.get("Study_Hours")
        Attendance_Percentage_value = request.form.get("Attendance_Percentage")
        Previous_Exam_Score_value = request.form.get("Previous_Exam_Score")
        Assignment_Completion_value = request.form.get("Assignment_Completion")
        #user_inputs = np.array([[Study_Hours_value,Attendance_Percentage_value,Previous_Exam_Score_value,Assignment_Completion_value]])
        user_inputs = pd.DataFrame({"Study_Hours": [Study_Hours_value],"Attendance_Percentage": [Attendance_Percentage_value],
        "Previous_Exam_Score": [Previous_Exam_Score_value],"Assignment_Completion": [Assignment_Completion_value]})
        predicted_value = model.predict(user_inputs)
        y_pred = model.predict(X)
        mae = mean_absolute_error(y,y_pred)
        mse = mean_squared_error(y,y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y,y_pred)

        figure = plt.figure(figsize=(10,5))
        sns.pairplot(student_df)
        plt.tight_layout()
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close() 
    
      # Convert the image memory to Base64 text
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    
      except ValueError:
         return render_template("index.html",predicted_value=f"All Fields are mandatory to be fill with some value.")
      except Exception as e:
         return render_template("index.html",predicted_value=f"ERR: {e}")
      
    return render_template("index.html",predicted_value=round(predicted_value[0],2),plot_url=plot_url,mae=f"{mae:.2f}",mse=f"{mse:.2f}",
                           rmse=f"{rmse:.2f}",r2=f"{r2:.4f}",intercept=f"{model.intercept_:.2f}",coefs=f"{model.coef_.round(2)}")


if __name__ == "__main__":
    app.run(debug=True)

