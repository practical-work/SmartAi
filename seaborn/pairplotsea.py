import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset("tips")
#print(data)
var = ["total_bill","size"]
# sns.pairplot(data)
# sns.pairplot(data,hue="sex")
# sns.pairplot(data,hue="sex",hue_order=["Female","Male"],palette="BuGn")
# sns.pairplot(data,hue="sex",hue_order=["Female","Male"],vars=var)
# sns.pairplot(data,hue="sex",hue_order=["Female","Male"],palette="Accent",x_vars=["size","tip"],kind="kde") #y_vars   kde - scatter,kde,hist,reg
sns.pairplot(data,hue="sex",hue_order=["Female","Male"],palette="Accent",x_vars=["size","tip"],kind="kde",
             diag_kind="hist") 

plt.show()
