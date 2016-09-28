import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def fun(x) :
    return x*(x-10)*(x+8)**2/1000
    
x = np.linspace(-15, 15, 100)

plt.plot(x, fun(x))

