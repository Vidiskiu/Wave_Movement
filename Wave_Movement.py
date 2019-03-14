import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def rotate(array, n):
    temp_y = array[n]
    for i in range(n, 0, -1):
        array[i] = array[i-1]
    array[0] = temp_y
    return array

def animate(i):
    # Setting up the shape
    x = np.linspace(0,2,1000)
    x1 = np.linspace(0, 1, 500)
    x2 = np.linspace(1, 2, 500)
    y1 = 2 * x1 - 1
    y2 = -2 * x2 + 3
    y = np.append(y1,y2)
    y = np.asfarray(y)
    y[y<0] = 0
    
    for i in range(i-1):
        y = rotate(y,int(y.shape[0])-1)

    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, interval=0.1, blit=True)

plt.show()