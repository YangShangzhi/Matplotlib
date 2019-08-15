import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6,dtype=int)
# print(x)
y = np.power(x,2)
# print(y)
plt.plot(x,y)
plt.show()