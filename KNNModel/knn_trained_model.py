import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import joblib


try:
    df = pd.read_csv("KNNModel/cleaned_titanic.csv",encoding="latin1")
    print("cleaned_titanic.csv file loaded successfully.")
except FileNotFoundError:
    print("ERR: No cleaned_titanic.csv named file found.")
    exit()


# separate features and target columns
X = df.drop(columns="Survived")
y = df["Survived"]


# Label Encoding sex - Male/Female
label_encoder = LabelEncoder()
X["Sex"] = label_encoder.fit_transform(X["Sex"])

# one hot encoding for Embarked(C/S/Q)
X = pd.get_dummies(X,drop_first=True,dtype=int)

# feature scaling using StandardScaler
standard_scaler = StandardScaler()
X[["Pclass","Age","SibSp","Parch","Fare"]] = standard_scaler.fit_transform(X[["Pclass","Age","SibSp","Parch","Fare"]])


# create model and fit training dataset
knn_model = KNeighborsClassifier(n_neighbors=7,weights="uniform",metric="minkowski",p=2,algorithm="auto")
knn_model.fit(X,y)


# Save trained model using joblib or pickle

joblib.dump(knn_model,"KNNModel/knn_trained_model.pkl")
joblib.dump(label_encoder, "KNNModel/label_encoder.pkl")
joblib.dump(standard_scaler, "KNNModel/standard_scaler.pkl")

