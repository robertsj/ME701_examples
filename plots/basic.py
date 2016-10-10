import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

x = np.linspace(0, 5)
y = np.sin(x)
z = np.cos(x)

plt.figure(1)
plt.plot(x, y, 'k-',
         x, z, 'b-.')
plt.legend(['sin(x)','cos(x)'])
plt.xlabel('x', fontsize=30)
plt.ylabel('y')
plt.title('some trig functions')

 