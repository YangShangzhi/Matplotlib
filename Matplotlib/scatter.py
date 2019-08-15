import matplotlib.pyplot as plt
import numpy as np

<<<<<<< HEAD
x = np.linspace(0,10,100)
siny = np.sin(x)

# plt.plot(x,siny)
plt.scatter(x,siny)
=======
x = np.linspace(0, 10, 100)
siny = np.sin(x)

# draw dotted line (same dot)
plt.plot(x,siny,'o')
# plt.scatter(x,siny)

>>>>>>> 877013df87d595040fc92a5983d51534fedbc52f
plt.show()