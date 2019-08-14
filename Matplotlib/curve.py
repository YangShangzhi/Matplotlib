import matplotlib.pyplot as plt
import numpy as np

def drawSpecCurve():
    x = np.linspace(0,10,100)
    siny = np.sin(x); cosy = np.cos(x)
    plt.plot(x, siny); plt.plot(x, cosy)

    plt.title("Special Curve");plt.xlabel("x")
    plt.show()

def drawCurve():
    x = range(-100, 100)
    y = [i**2 for i in x]
    plt.plot(x, y)

    plt.title("Curve");plt.xlabel("x");plt.ylabel("y = x^2")

    # save the image
    # plt.savefig("CurveResult")
    plt.show()

drawSpecCurve()