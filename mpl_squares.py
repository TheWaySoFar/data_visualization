import matplotlib
import matplotlib.pyplot as plt
values = [x for x in range(10)]
squares = [x**2 for x in range(10)]

plt.plot(values,squares,linewidth=5)
plt.title("Square numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()