import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

plt.plot(x,x+0,'--g', label="--g")
plt.plot(x,x+1,'-.r', label="-.r")
plt.plot(x,x+2,':b', label=":b")
plt.plot(x,x+3,'.k', label=".k")
plt.plot(x,x+4,',c', label=",c")
plt.plot(x,x+5,'*y', label="*y")

# 
plt.legend(loc='upper left', fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.show()