import matplotlib.pyplot as plt

x = [1,2,3,4]
y = ["s1","s2","s3","s4"]

fig = plt.figure(figsize=(10,5),num="Subplots & layout adjustments")
fig.suptitle("Multiple Plots on Same Page ")
fig.set_label("Graphs")

plt.subplot(2,2,1)
plt.plot(x,y)
plt.text(1,"s2","text line") # use ha="center/left/right"-horizontal alignment similarlly for va
plt.title("Line graph")

plt.subplot(2,2,2)
plt.bar(x,y)
plt.annotate("pointing",xy=(2,"s1"),xytext=(2,"s3"),arrowprops={"arrowstyle":"->","color":"red"})
plt.title("Bar graph")                                             # <->,-|>,<-,fancy,simple,wedge

plt.subplot(2,2,3)
plt.pie(x,labels=y,autopct="%1.1f%%")
plt.title("Pie chart")

plt.subplot(2,2,4)
plt.hist(x,bins=10)
plt.title("Histogram")

plt.tight_layout()  # use fig.subplots_adjust(left=value,right,...,bootom,top,wspace,hspace)
plt.savefig("subplot-layout-adjustments.png",dpi=300,bbox_inches='tight')
plt.show()

