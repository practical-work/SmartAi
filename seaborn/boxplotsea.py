import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")
#print(data)
#sns.set_theme(style="whitegrid")
orders = ["Fri","Sat","Thur","Sun"]
#sns.boxplot(x="day",y="total_bill",data=data)
#sns.boxplot(x="day",y="total_bill",data=data,order=orders)
sns.boxplot(x="day",y="total_bill",data=data,hue="time",palette="plasma",linewidth=1,showmeans=True,
            meanprops = {"marker":"s","markeredgecolor":"w","markersize":5},orient="v"
            )  # orient = "h" for this numerical data on both axes must

# sns.boxplot(x=data["size"])
# sns.boxplot(y=data["size"])
plt.show()
