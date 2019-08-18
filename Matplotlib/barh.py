import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

x = np.arange(5,dtype=int)
y = np.random.randint(-5,5,5)

# divide canvas into 2 part
plt.subplot(1,2,1)
plt.bar(x,y,color='blue')
# draw a line
plt.axhline(0,color="blue",linewidth=2)
    
plt.subplot(1,2,2)
plt.barh(x,y,color='red')
plt.axvline(0,color="red",linewidth=2)

plt.show()