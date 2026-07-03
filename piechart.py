import matplotlib.pyplot as plt

categories = ["Rent","Food","Transport","Entertainment","Savings"]
expenses = [18000,8000,3000,4000,7000]

fig = plt.figure(figsize=(10,5))
fig.suptitle("Pie Chart")
colors = ["green","red","blue","gray","orange"]
wedges,texts,autotexts=plt.pie(expenses,labels=categories,autopct="%1.1f%%",explode=(0.1,0,0,0,0),colors=colors,
        wedgeprops={"edgecolor":"whitesmoke"},textprops={"color":"#fff","fontsize":12},counterclock=False
        ,shadow=False)
for wedge in wedges:
    wedge.set_alpha(0.7)

plt.title("Monthly Budget")
plt.xlabel("Expenses")
plt.ylabel("Categories")
plt.legend()
plt.axis("equal")
plt.tight_layout()
plt.show()