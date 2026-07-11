import joblib
import pandas as pd
from flask import Flask,render_template,request
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)

# Create web application
app = Flask(__name__)

# Loading trained model files
try:
    with open("knn_trained_model.pkl","rb") as file1:
        knn_model = joblib.load(file1)
    with open("label_encoder.pkl","rb") as file2:
        label_encoder = joblib.load(file2)
    with open("standard_scaler.pkl","rb") as file3:
        standard_scaler = joblib.load(file3)
    
except Exception as e:
    print(e)


# Read cleaned_titanic.csv file
try:
    df = pd.read_csv("cleaned_titanic.csv",encoding="latin1")
    print("cleaned_titanic.csv file loaded successfully.")
except FileNotFoundError:
    print("ERR: No cleaned_titanic.csv named file found.")


# separate features and target columns
X = df.drop(columns="Survived")
y = df["Survived"]

# Label Encoding sex - Male/Female
X["Sex"] = label_encoder.fit_transform(X["Sex"])

# one hot encoding for Embarked(C/S/Q)
X = pd.get_dummies(X,drop_first=True,dtype=int)

# feature scaling using StandardScaler
X[["Pclass","Age","SibSp","Parch","Fare"]] = standard_scaler.fit_transform(X[["Pclass","Age","SibSp","Parch","Fare"]])



y_pred = knn_model.predict(X)

# Web application Routing
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/classification",methods=["POST"])
def classification():
    if(request.method == "POST"):
        pclass = request.form.get("pclass")
        sex = request.form.get("sex")
        age = float(request.form.get("age"))
        sibsp = int(request.form.get("sibsp"))
        parch = int(request.form.get("parch"))
        fare = float(request.form.get("fare"))
        embarked = request.form.get("embarked")

        # label encode user sex input
        le_sex = label_encoder.transform([sex])[0]

        # Handle embarked (c/s/q) logic
        embarked_S = 0
        embarked_Q = 0
        if embarked == "S":
           embarked_S = 1
        elif embarked == "Q":
           embarked_Q = 1
        # If embarked == "C", both remain 0

        # feature scaling rest input values
        scale_df = pd.DataFrame({
            "Pclass": [pclass],
            "Age": [age],
            "SibSp": [sibsp],
            "Parch": [parch],
            "Fare": [fare] })
        scaled = standard_scaler.transform(scale_df)
        pclass, age, sibsp, parch, fare = scaled[0]   

        # Make prediction whether Survived or Not
        predict_df = pd.DataFrame({"Pclass": [pclass],"Sex": [le_sex],"Age": [age],
        "SibSp": [sibsp],"Parch": [parch],"Fare": [fare],"Embarked_Q": [embarked_Q],
        "Embarked_S": [embarked_S] })
        prediction = knn_model.predict(predict_df)[0]

        accuracy = accuracy_score(y, y_pred)
        precision = precision_score(y, y_pred)
        recall = recall_score(y, y_pred)
        f1 = f1_score(y, y_pred)
        cm = confusion_matrix(y, y_pred)
        cr = classification_report(y, y_pred)


    return render_template("index.html",prediction=prediction,accuracy=f"{accuracy:.2f}",precision=f"{precision:.2f}",recall=f"{recall:.2f}",f1=f"{f1:.4f}",cm=cm,cr=cr)



if __name__ == "__main__":
    app.run(debug=True)



