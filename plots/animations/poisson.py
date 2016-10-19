import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
This script will solve the Poisson equation (d^2 T / dx^2 + d^2 T / dy^2 = -Q)
on a grid and animate the solution as it converges.  Assume dx=dy=L/N, where
L is the side length, and N is the number of cells in a direction.
'''

N = 40
dx = 1.0 / N
Q = 10

# Initialize T to be one everywhere
T = np.ones((N,N))

def update_T(T):
    # This is a generator that will solve the Poisson equation and pause at
    # each iteration for plot creation
    yield T
    while True:
        for i in range(1,N-1):  # loop in x-direction
            for j in range(1,N-1):  # loop in y-direction
                T[i,j] = 0.25 * (T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1] + Q * dx**2)
        # send back T, but save current position.  Continues on where it left off
        # if the function is called again
        yield T
    
def update(*args):
    global data
    im.set_array(data.next())
    fig.canvas.draw()
    return im,    
    
# Initialize the figure environment
fig = plt.figure()
# Initialize generator
data = update_T(T)
# Draw the initial image
im = plt.imshow(data.next(), cmap=plt.get_cmap('viridis'), animated=True, vmin=1, vmax=1.7)
# Create the animation
ani = animation.FuncAnimation(fig, update, interval=0.001, blit=True)
plt.show()
