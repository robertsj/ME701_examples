import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
This function will take data that is complete at the time of making the plot.
It generates an image for each timestep (or whatever you want to animate), and
creates the animation from the list of images.
'''

def make_data():
    # randomly generate a 30x30 array of numbers between 0 and 1
    return np.random.random((30,30))
    
def time_dep(f, t_max=100.0, dt=1.0):
    '''
    Creates an array that contains all time dependent data
    
    f is a function that will generate the data for a given time step
    '''
    # Initialize a blank list
    data = []
    # Loop over the number of time steps
    for i in np.linspace(0,t_max,t_max/float(dt)):
        # Append the new time step data to our list
        data.append(f())
    # convert the list to an array and return it
    return np.array(data)

def make_2D_imshow(data):
    # create a new blank list to contain all the plots
    im = []
    # loop over the number of time steps
    for i in range(len(data)):
        # Create a new plot
        plot = plt.imshow(data[i])
        # Make a tuple out of the plot and append it to the list
        im.append((plot,))
    # create the figure for the animation
    fig = plt.figure(0)
    # create the animation
    ani = animation.ArtistAnimation(fig, im, interval=100, blit=True)
    plt.show()
    
make_2D_imshow(time_dep(make_data))
