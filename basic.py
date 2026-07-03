import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [9,3,5,6]

plt.plot(x,y,label="Marks vs Score")
plt.scatter(x,y)
plt.xlabel("Score in last 4 TESTs")
plt.ylabel("Marks Obtained")
plt.xlim(0,5)
plt.ylim(0,15)
plt.xticks([1,2,3,4],["t1","t2","t3","t4"])
plt.title("Student performance in Test")
plt.legend()
plt.show()