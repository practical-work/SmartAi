import matplotlib.pyplot as plt

marks = [45,52,67,70,73,80,85,91,98]

fig = plt.figure(figsize=(10,5))
fig.suptitle("Histogram Chart")
plt.hist(marks,bins=8,rwidth=0.7,color="darkred",alpha=0.8,edgecolor="whitesmoke",linewidth=1,
         histtype="barstacked",cumulative=True,density=True,orientation="horizontal",label="Marks")
plt.title("Marks Distribution")
plt.ylabel("Marks")
plt.xlabel("Intervals")
plt.legend()
plt.tight_layout()
plt.show()