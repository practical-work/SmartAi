import matplotlib.pyplot as plt

fig,ax = plt.subplots(2,2,figsize=(10,2),num="Subplots")
fig.suptitle("Subplots on ONE PAGE")

x = [1,2,3,4]
y = ["s1","s2","s3","s4"]

ax[0,0].plot(x,y,label="num")
ax[0,0].set_title("Line Graph")
ax[0,0].set_xlabel("Numbers")
ax[0,0].set_ylabel("S series")
ax[0,0].grid(True)
ax[0,0].legend()

ax[0,1].bar(x,y)
ax[0,1].set_title("Bar graph")

ax[1,0].pie(x,labels=y,autopct="%1.1f%%")
ax[1,0].set_title("Pie chart")


ax[1,1].hist(x,bins=10)
ax[1,1].set_title("Histogram")

# fig.delaxes(ax[1,1]) # remove  empty plot or use ax[1,1].axis("off")
#plt.tight_layout()
fig.subplots_adjust(
    left=0.08,
    right=0.97,
    top=0.82,
    bottom=0.15,
    wspace=0.35,
    hspace=0.70
)

plt.savefig("subplots.pdf",dpi=300,bbox_inches='tight') #svg,pdf,png
plt.show()
