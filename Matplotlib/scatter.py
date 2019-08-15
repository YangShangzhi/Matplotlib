import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
siny = np.sin(x)

# plt.plot(x,siny)
plt.scatter(x,siny)
plt.show()