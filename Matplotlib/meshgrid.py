import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = np.linspace(-10,10,100)

X,Y = np.meshgrid(x,y)

Z = np.sqrt(x**2 + Y**2)

# plt.contour(X,Y,Z)
plt.contourf(X,Y,Z)
plt.show()