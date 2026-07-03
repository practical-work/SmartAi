import matplotlib.pyplot as plt

ad_cost = [5,10,15,20,25,30,35,40,45,50]
sales = [20,28,35,45,55,68,75,85,95,108]

figure = plt.figure(figsize=(10,5))
figure.suptitle("Scatter Plot")
plt.scatter(ad_cost,sales,label="Cost vs Sales",marker="+",color = "darkgreen")
plt.xlabel("Advertisement Cost",fontsize=12,color="g")
plt.ylabel("Sales",fontsize=12,color="g")
plt.title("Advertisement Cost vs Sales",color = "darkblue")
plt.legend(fontsize=7,loc="upper left")
plt.tight_layout()
plt.show()