import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

df = pd.read_csv("LogisticRegressionModel/spam.csv",encoding="latin1")
# print(df.sample(5))

#print(df.head())

# print(df.columns)
# print(df.shape)

#print(df.duplicated().sum())
# remove duplicates rows
df.drop_duplicates(inplace=True,ignore_index=True)
#print(df.duplicated().sum())

# print(df.shape)
# print(df.isnull().sum())


# drops unwanted cols

df.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"],inplace=True)

# print(df.isnull().sum())
# print(df.head())

# Renaming of cols with meaningfull and usefull names

df.rename(columns={"v1":"label","v2":"message"},inplace=True)
# print(df.head())


# label encoding for label cols(spam,ham(Not Spam))
label_encoder_obj = LabelEncoder()

df["label"]=label_encoder_obj.fit_transform(df["label"])  # 0 - Ham & 1 - Spam
#print(df.head())


# EDA

counts = df["label"].value_counts()
#print(counts)  # Ham is more than spam so, it is a imbalance dataset

# plt.pie(counts,labels=["ham","spam"],autopct="%0.2f")
# plt.show()


df.to_csv("LogisticRegressionModel/sms_spam.csv",index=False)
