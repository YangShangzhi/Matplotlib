import matplotlib.pyplot as plt
import numpy as np

# comfirm everytime the same value x or y can get
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# generate 10 points' size
size = np.random.rand(10) * 500

# generate 100 colors
# the number of color must equal to the number of point
color = np.random.rand(100)

plt.scatter(x,y,s=size,c=color,alpha=0.7)
plt.show()