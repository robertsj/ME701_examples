from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a = 0.5
k = 7
d = 8

def f(t):
    # This is the function that we want to plot
    F = (a + np.cos(k / d * t))
    x = F * np.cos(t)
    y = F * np.sin(t)
    return x, y
    
def f(t):
    # This is another function that we want to plot
    x = np.sin(t) * np.cos(-7*t/16) - 0.25 * np.cos(t) * np.sin(-7*t/16)
    y = np.sin(t) * np.sin(-7*t/16) - 0.25 * np.cos(t) * np.cos(-7*t/16)
    return x, y
    
    
# Define the t value  
t = 0
# get initial function values
x, y = f(t)

# Initialize the figure environment
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect('equal')
r = np.sqrt(x**2+y**2)
r = 1
ax.axis([-r,r,-r,r])
ax.grid(True)
# Get the line object from the figure
line, = ax.plot(x, y, 'm-')

def updatefig(*args):
    # Update the plot for the next image
    global t  # Allow editing the x in the global scope
    # update x
    t += 0.03
    # change the data on the line
    x, y = f(t)
    X = np.append(line.get_xdata(), x)
    Y = np.append(line.get_ydata(), y)
    line.set_xdata(X)
    line.set_ydata(Y)
    # redraw the plot
    fig.canvas.draw()
    # send back the line as a 
    return line,
    
# Create the animation
ani = animation.FuncAnimation(fig, updatefig, interval=3, blit=True)
# To save, requires libav-tools to be installed
#ani.save('name.mp4', writer='avconv')
plt.show()
