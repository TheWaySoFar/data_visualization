from matplotlib import pyplot as plt
from randwalk import RandomWalk

while True:
    rw = RandomWalk(num_points=50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))
    plt.scatter(rw.x_args,rw.y_args,c=list(range(rw.num_points)),cmap=plt.cm.Blues,s=1)
    plt.scatter(0,0,c='red',s=100)
    plt.scatter(rw.x_args[-1],rw.y_args[-1],c='green',s=100)
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break