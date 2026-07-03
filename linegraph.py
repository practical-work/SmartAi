import matplotlib.pyplot as plt

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temperature = [31,33,35,34,36,38,37]

figure = plt.figure(figsize=(10,5))
figure.suptitle("Line Graph")
plt.plot(days,temperature,color="darkred",label="Temperature (7 Days)",linestyle="--",marker="o",linewidth=1,markersize=7)
plt.xlabel("Days",fontsize=12)
plt.ylabel("Temperature",fontsize=12)
plt.title("Temperature in 7 Days")
plt.grid(True,linestyle="--",alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()