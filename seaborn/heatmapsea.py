import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("anagrams")
#print(sns.get_dataset_names())
#print(df)

data = df.drop("attnr",axis=1).head()  # head used for taking first 10 rows only
#print(data)
arr = [['a1','a2','a3','a4'],['b1','b2','b3','b4'],['c1','c2','c3','c4'],['d1','d2','d3','d4'],['e1','e2','e3','e4'],]
# sns.heatmap(data=data,annot=True,vmin=0,vmax=10,cmap="gist_heat",annot_kws={"fontsize":12,"color":"w"},
#             linewidths=1,linecolor="whitesmoke",cbar=True)

# sns.heatmap(data=data,annot=arr,fmt="s",vmin=0,vmax=10,cmap="gist_heat",annot_kws={"fontsize":12,"color":"w"},
#             linewidths=1,linecolor="whitesmoke",cbar=True)

heatmap_1 = sns.heatmap(data=data,annot=arr,fmt="s",vmin=0,vmax=10,cmap="PuOr",annot_kws={"fontsize":12,"color":"b"},
            linewidths=1,linecolor="whitesmoke",cbar=True,xticklabels=False,yticklabels=False)

heatmap_1.set(xlabel = "X axis",ylabel = "Y axis")
sns.set_theme(font_scale=2)
plt.show()

