import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("penguins") 
#print(df) 
order_x = ['Dream','Biscoe','Torgersen']
order_y = ['Female','Male']
sns.set_theme(style="darkgrid")
sns.barplot(x ="island",y="body_mass_g",data=df,hue="sex",order=order_x,hue_order=order_y,palette="Accent",
            saturation=100,alpha = 0.6,edgecolor = "gray",orient="v",weights = 8,err_kws={'color': 'black','linewidth':1},
        errorbar=('ci', 77),capsize=0.1,dodge=True)  #n_boot = 0-100 value dodge means overlapping male & female to find difference by default True
plt.show()