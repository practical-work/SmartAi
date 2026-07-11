import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
try:
    df = pd.read_csv("KNNModel/train.csv",encoding="latin1")
    print("train.csv file loaded successfully.")
except FileNotFoundError:
    print("ERR: No train.csv named file found.")
    exit()

# print(df.head())

# print(df.shape,df.columns)

# print(df.duplicated().sum())

# print(df.isnull().sum())

# drops column not always required for user input and predictions
df.drop(columns=["PassengerId","Name","Ticket","Cabin"],inplace=True)

#print(df.tail(3))

df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#print(df.isnull().sum())
#print(df.sample(5))

# print(df.head())

# print(df.info())
# print(df.describe())


# EDA

sex_counts = df["Sex"].value_counts()

# plt.pie(sex_counts,labels=["Male","Female"],autopct="%0.2f")
# plt.show()


survivals_count = df["Survived"].value_counts()

# plt.pie(survivals_count,labels=["Survived","Not Survived"],autopct="%0.2f")
# plt.show()


# sns.scatterplot(x=df["Age"],y=df["Fare"],hue=df["Sex"])
# plt.show()


df.to_csv("KNNModel/cleaned_titanic.csv",index=False)