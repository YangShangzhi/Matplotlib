import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6,dtype=int)
y = np.power(x,2)

# design line sheet
plt.plot(x,y,linewidth=5)

# set Chinese code
# plt.rcParams['font.sans-serif']=['SimHei']

plt.title('Polygonal Chart')
plt.xlabel("x")
plt.ylabel("y = x^2")


plt.show()