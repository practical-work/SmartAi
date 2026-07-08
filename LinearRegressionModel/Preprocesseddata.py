import pandas as pd

df = pd.read_csv("student_performance_dataset.csv",encoding="latin1") 

# print(df.head())

df.drop_duplicates(inplace=True)

# print(df.isnull().sum())

df["Attendance_Percentage"] = df["Attendance_Percentage"].interpolate(method="linear")

df["Assignment_Completion"] = df["Assignment_Completion"].fillna(df["Attendance_Percentage"].mean())

print(df.head(20))
print(df.isnull().sum())

# print(df.info())
# print(df.describe())

df.to_csv("LinearRegressionModel/Student_Performance_Data.csv",index=False)
