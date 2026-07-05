import seaborn as sns
import matplotlib.pyplot as plt


tips = sns.load_dataset("tips")  # seaborn provides some builtin datasets for practice , use your own by pandas dataframe
tips = tips.sort_values("total_bill") # sorting tips column name total_bill for linear plotting
sns.lineplot(x ="tip",y="total_bill",data=tips,hue="size",size=25,palette="Accent",markers=["o","s","D",">","<","d"],legend=True,
             style="size",dashes=True)
"""sns.scatterplot(x ="tip",y="total_bill",data=tips,hue="size",size=25,palette="Accent",markers=["o","s","D",">","<","d"],legend=True,
             style="size")"""
plt.show()