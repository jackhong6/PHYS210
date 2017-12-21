import numpy as np
import matplotlib.pyplot as plt

plotfig = False

n = 6000
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
z = np.zeros((n,n))
for k in range(n):
    for m in range(n):
        z[k,m] = np.exp(-(x[m]**2 + y[k]**2))

if plotfig:
    plt.figure(1)
    plt.imshow(z,extent=(-3,3,-3,3))
    plt.savefig("2dexp_loops.pdf")
    plt.show()
