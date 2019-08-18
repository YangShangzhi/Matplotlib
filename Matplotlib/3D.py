import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X = [1,1,2,2]
Y = [3,4,4,3]
Z = [1,100,1,1]

figure = plt.figure()

ax = Axes3D(figure)
ax.plot_trisurf(X,Y,Z)

plt.show()