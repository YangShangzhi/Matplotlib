import numpy as py
import matplotlib.pyplot as plt

x = [1980,1985,1990,1995]
x_label = ['1980y','1985','1990y','1995y']
y = [1000,3000,4000,5000]

plt.bar(x,y,width=3)
plt.xticks(x,x_label)
plt.xlabel("Year")
plt.ylabel("Sale Volumn")
plt.title("Year - Sale")
plt.show()
