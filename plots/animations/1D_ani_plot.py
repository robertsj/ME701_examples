import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def f(x):
    # This is the function that we want to plot
    return np.sin(x)

# Define the x values
x = np.linspace(0, 2 * np.pi, 120)

# Initialize the figure environment
fig = plt.figure()
ax = fig.add_subplot(111)
# Get the line object from the figure
line, = ax.plot(x, f(x))

def updatefig(*args):
    # Update the plot for the next image
    global x  # Allow editing the x in the global scope
    # update x
    x += np.pi / 15.
    # change the data on the line
    line.set_ydata(f(x))
    # redraw the plot
    fig.canvas.draw()
    # send back the line as a 
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
# To save, requires libav-tools to be installed
#ani.save('name.mp4', writer='avconv')
plt.show()
