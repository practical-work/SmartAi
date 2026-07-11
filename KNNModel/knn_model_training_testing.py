import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix,classification_report)
import joblib


try:
    df = pd.read_csv("KNNModel/cleaned_titanic.csv",encoding="latin1")
    print("cleaned_titanic.csv file loaded successfully.")
except FileNotFoundError:
    print("ERR: No train.csv named file found.")
    exit()


# separate features and target columns
X = df.drop(columns="Survived")
y = df["Survived"]

# Splits data in training & testing phase

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Label Encoding sex - Male/Female
label_encoder = LabelEncoder()
X_train["Sex"] = label_encoder.fit_transform(X_train["Sex"])
X_test["Sex"] = label_encoder.transform(X_test["Sex"])

# one hot encoding for Embarked(C/S/Q)
X_train = pd.get_dummies(X_train,drop_first=True,dtype=int)
X_test = pd.get_dummies(X_test,drop_first=True,dtype=int)
X_train, X_test = X_train.align(
    X_test,
    join="left",
    axis=1,
    fill_value=0
)

# feature scaling using StandardScaler
standard_scaler = StandardScaler()
X_train[["Pclass","Age","SibSp","Parch","Fare"]] = standard_scaler.fit_transform(X_train[["Pclass","Age","SibSp","Parch","Fare"]])
X_test[["Pclass","Age","SibSp","Parch","Fare"]] = standard_scaler.transform(X_test[["Pclass","Age","SibSp","Parch","Fare"]])


# print(X_train)
# print("\n")
# print(X_test)

# create model and fit training dataset
knn_model = KNeighborsClassifier(n_neighbors=7,weights="uniform",metric="minkowski",p=2,algorithm="auto")
knn_model.fit(X_train,y_train)

y_pred = knn_model.predict(X_test)

# print(y_pred)


# Performance Evaluation for KNN Classification Model

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
recall = recall_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)
cr = classification_report(y_test,y_pred)

print(f" Accuracy : {accuracy:.2f}")
print(f" Precision : {precision:.2f}")
print(f" Recall : {recall:.2f}")
print(f" F1 Score : {f1:.4f}")
print(f"Confusion Matrix \n {cm}")
print(f"Classification Report \n {cr}")


# Save trained model using joblib or pickle

# joblib.dump(knn_model,"KNNModel/knn_trained_model_testing.pkl")
# joblib.dump(label_encoder, "KNNModel/label_encoder_testing.pkl")
# joblib.dump(standard_scaler, "KNNModel/standard_scaler_testing.pkl")