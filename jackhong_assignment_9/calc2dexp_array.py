import numpy as np
import matplotlib.pyplot as plt

plotfig = False

x1d=np.linspace(-3,3,6000)
y1d=np.linspace(-3,3,6000)
x2d,y2d=np.meshgrid(x1d,y1d)
r2d=x2d**2+y2d**2
z=np.exp(-r2d)

if plotfig:
    plt.figure(1)
    plt.imshow(z,extent=(-3,3,-3,3))
    plt.savefig("2dexp_array.pdf")
    plt.show()
