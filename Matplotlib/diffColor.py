import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.arange(5,dtype=int)
y = np.random.randint(-5,5,5)

v_bar = plt.bar(x,y,color='blue')
for x_bar, height in zip(v_bar, y):
    if height > 0:
        x_bar.set(color='red')
        
# draw a line
plt.axhline(0,color="blue",linewidth=2)

plt.show()