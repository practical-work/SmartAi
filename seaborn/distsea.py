import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")

sns.displot(tips["size"],bins =[1,2,3,4,5,6],color="orange",edgecolor = "gray",kde = True,rug = True,log_scale=False,alpha = 0.3)
plt.show()