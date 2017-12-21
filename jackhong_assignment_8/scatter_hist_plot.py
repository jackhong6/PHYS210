# PHYS 210: Assignment 8, Problem 2
# Jack Hong, 30935134
# Oct. 4, 2016
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

mean = [0,0]
cov = [[1,0],[0,1]]
x,y = np.random.multivariate_normal(mean, cov, 1000).T

plt.figure(1)
scatter = plt.scatter(x,y,marker='.')
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("bivariate_scatter_plot.pdf")

plt.figure(2)
plt.subplot(211)
x_hist = plt.hist(x)
plt.xlabel("x")
plt.subplot(212)
y_hist = plt.hist(y)
plt.xlabel("y")
plt.savefig("bivariate_hist_plot.pdf")

plt.figure(3)
plt.subplot(221)
plt.scatter(x,y,marker='.')
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(222)
plt.hist(y)
plt.xlabel("y")

plt.subplot(223)
plt.hist(x)
plt.xlabel("x")
plt.savefig("scatter_hist_plot.pdf")

plt.show()
