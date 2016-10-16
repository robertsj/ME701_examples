import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d

'''
This script creates a spiral that spins
'''

def get_xy(t):
    # Defines the equation for a spiral in parametric form
    a = 0.15
    b = 0.03
    # Hold the exponential term constant by defining t_prime != t
    t_prime = np.linspace(0,150,1000)
    x = a * np.cos(t) * np.exp(b * t_prime)
    y = a * np.sin(t) * np.exp(b * t_prime)
    return x, y
    
def updatefig(*args):
    # Vary the current time to plot
    global t
    t += 1
    # get the updated function values
    x, y = get_xy(t)
    # update the plot data
    line.set_xdata(x)
    line.set_ydata(y)
    # redraw the figure
    fig.canvas.draw()
    # return the line
    return line,
    
t = np.linspace(0,40,1000)
x, y = get_xy(t)
    
# create the initial figure
fig = plt.figure()
ax = fig.add_subplot(111)
# set the axis
plt.axis([-10,10,-10,10])
line, = ax.plot(x, y)
    
# create the animation
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
