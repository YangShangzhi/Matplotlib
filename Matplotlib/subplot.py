import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
siny = np.sin(x)
cosy = np.cos(x)

# divide plot into 2x2 area, and plot into 1st subarea
plt.subplot(2,2,1)
# modify x.y axis
plt.xlim(-5,20)
plt.ylim(-2,2)
plt.plot(x, siny)


# plot into 3rd subarea
plt.subplot(2,1,2)
plt.plot(x,cosy)

plt.show()