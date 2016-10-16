import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
This script creates a spiral that grows outwards
'''

def get_xy(t):
    # Defines the equation for a spiral in parametric form
    a = 0.5
    b = 0.05
    x = a * np.cos(t)*np.exp(b*t)
    y = a * np.sin(t)*np.exp(b*t)
    return x, y
    
def updatefig(*args):
    # access the maximum time to plot
    global t_max
    # increase the maximum
    t_max += 0.1
    # get the updated x and y values for that t
    x, y = get_xy(np.linspace(0,t_max,1000))
    # update the data in the plot
    line.set_xdata(x)
    line.set_ydata(y)
    fig.canvas.draw()
    # return the line back to animation
    return line,
    
# initialize the maximum time and x and y values
t_max = 0
x, y = get_xy(np.linspace(0,t_max,1000))
    
# create the animation figure
fig = plt.figure()
ax = fig.add_subplot(111)
# Set the axis for the plot
plt.axis([-10,10,-10,10])
line, = ax.plot(x, y)
    
# Create the animation
ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)
plt.show()
