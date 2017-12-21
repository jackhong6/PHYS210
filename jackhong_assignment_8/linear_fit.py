# PHYS 210: Assignment 8, Problem 1
# Jack Hong, 30935134
# Oct 4, 2016

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as spopt

data = np.loadtxt("data.txt", usecols=(1,2,4)) # import x, y, and y_err
x,y,y_err = data[:,0], data[:,1], data[:,2]

def lin_func(x,b,c):
    # Linear function with y intercept c and slope c
    return b*x + c

fit = spopt.curve_fit(lin_func, x, y, sigma=y_err, absolute_sigma=True)[0]

d = plt.errorbar(x, y, y_err, fmt="ro", label="Data")
f = plt.plot(x, lin_func(x,fit[0], fit[1]), label="Fit")

plt.xlim(1.23, 1.36)
plt.title("PHYS 210, Lab 8: Linear fit of given sample data")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="best")
plt.savefig("linear_fit.pdf")
plt.show()
