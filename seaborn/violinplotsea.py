import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")
#print(data)

# sns.violinplot(x="day",y = "total_bill",data=data,palette="PuOr",hue="time",saturation=100,linewidth=1,linecolor="g",
#               inner="box",density_norm='width')
sns.violinplot(x="day",y = "total_bill",palette="PuOr",hue="sex",data=data,saturation=100,linewidth=1,linecolor="g",
              inner="stick",split=True)

# sns.violinplot(x = data["tip"])
# sns.violinplot(y = data["tip"])
plt.show()