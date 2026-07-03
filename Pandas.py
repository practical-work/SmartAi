import pandas as pd
import numpy as np
series = pd.Series([2,4,7,8])
# print(series)


data = {
    "Student Name":["Ram","Shayam","Sita","Hanuman","Krishna","Balram"],
    "Age":[23,18,20,17,20,22],
    "Roll No":[24,55,29,72,26,36]
}

df = pd.DataFrame(data)
# print(df)

# to_csv,to_json,to_excel,to_html
#df.to_csv("Student-detail.csv",index=False)

# read_csv,read_json,read_excel,read_html,read_sql
df1 = pd.read_csv("output.csv",encoding="latin1")  # encoding = "utf-8"
# print(df1)


# print(df.head())  #df.head(value) by-default=5 starting rows
# print(df.tail())  #df.tail(value) by-default=5 ending rows
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print(df.dtypes)

# print(df["Age"])
# print(df[["Student Name","Age"]])
# print(df[df["Age"]>20])  #Boolean masking
# print(df[(df["Age"]>20) & (df["Roll No"] < 40)])


# Adding new column
df["Fees Status"] = [0,1,0,0,0,1]
# print(df)

df.insert(0,"College Name","xyz")
# print(df)

df["Eligible for Vote"] = ["Yes" if (x >= 18) else "No" for x in df["Age"] ]
# print(df)

# Update any value 
df.loc[1,"Fees Status"] = 0
# print(df)

# remove column
df.drop(columns=["Eligible for Vote"],inplace=True)
# print(df)

df3 = df.drop(columns=["Age","Fees Status"],inplace=False)
# print(df3)

# remove row using index value
df4 = df.drop(5,inplace=False)
# print(df4)

df5 = df.drop([5,2],inplace=False)
df5.reset_index(drop=True,inplace=True)
# print(df5)

# Handling missing values
student_data = {
    "Student Name":["Ram","Ram","Shayam",None,"Hanuman","Krishna","Balram"],
    "Age":[23,23,None,20,17,None,22],
    "Roll No":[24,24,None,29,72,26,36]
}
df6 = pd.DataFrame(student_data)
# print(df6)

# Remove duplicates rows
df6.drop_duplicates(inplace=True,ignore_index=True)
# print(df6)

# print(df6.isnull())
# print(df6.isnull().sum())

#print(df6.dropna(axis=0,inplace=False,ignore_index=True))

#print(df6.fillna(0,inplace=False))

#print(df6["Age"].fillna(df6["Age"].mean(),inplace=False))

# Interpolation methods= linear,polynomial,time etc.
df6.loc[2,"Student Name"] = "Sita"
numeric_cols = df6.select_dtypes(include="number").columns
df6[numeric_cols] = df6[numeric_cols].interpolate(method="linear")
# print(df6)

# Sorting , Aggregation & Grouping

#print(df6.sort_values(by="Age",ascending=True,inplace=False,ignore_index=True))

#print(df6.sort_values(by=["Student Name","Age"],ascending=False,inplace=False,ignore_index=True))

# aggreation - min,max,count,sum,mean,std,var etc.
# print(df6["Age"].std())

# grouping
grouped0 = df6.groupby("Age")["Roll No"].sum()
# print(grouped0)

grouped1 = df6.groupby(["Age","Student Name"])["Roll No"].sum()
# print(grouped1)

# Merging and Joining & how="inner or outer or cross or left or right"

#print(pd.merge(df,df6,on="Student Name",how="inner"))
# print(pd.merge(df,df6,on="Student Name",how="outer"))
# print(pd.merge(df,df6,on="Student Name",how="left"))
# print(pd.merge(df,df6,on="Student Name",how="right"))
# print(pd.merge(df,df6,how="cross"))

# Concatination
#print(pd.concat([df,df6],axis=0,ignore_index=True))

df7=df6.to_numpy()
#print(df7)
