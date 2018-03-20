import matplotlib.pyplot as plt

xargs = list(range(1,1001))
yargs = [x**2 for x in range(1,1001)]
#xargs = list(range(1,5))
#yargs = list(range(1,5))
plt.scatter(xargs,yargs,c='red',s=200)
plt.title("Scatter squares")
plt.xlabel("Num",fontsize=14)
plt.ylabel("Square",fontsize=14)
plt.tick_params(axis='both',which='both',labelsize=14)

#plt.axis([0,1100,0,1100000])
plt.show()
#plt.savefig('scatter_squares.pdf')