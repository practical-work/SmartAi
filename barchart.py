import matplotlib.pyplot as plt

subjects = ["Math","Science","English","Computer","History"]
marks = [92,88,81,95,76]

fig = plt.figure(figsize=(10,5))
fig.suptitle("Bar Chart")
plt.bar(subjects,marks,width=0.5,color="chocolate",label="Student Marks",alpha=0.5,edgecolor="black",linewidth=0.5)
#plt.grid(True,color="gray",alpha=0.3,linewidth=1,linestyle=":")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0,100)
plt.title("Student Marks by Subjects")
plt.legend()
plt.show()