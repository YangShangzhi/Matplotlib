import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
siny = np.sin(x)

# draw dotted line (same dot)
plt.plot(x,siny,'o')
# plt.scatter(x,siny)

plt.show()