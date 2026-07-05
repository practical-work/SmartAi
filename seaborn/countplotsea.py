import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")
#print(data)

sns.countplot(x="sex",data=data,palette="Accent",hue="smoker",saturation=100,edgecolor="black")
#sns.countplot(y="sex",data=data,palette="Accent",hue="smoker",saturation=100,edgecolor="black")
plt.show()