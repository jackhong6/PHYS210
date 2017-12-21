# PHYS 210, Assignment 10: Part 2, Numerical Integration I
# Jack Hong, 30935134
# October 12, 2016
import numpy as np
import matplotlib.pyplot as plt

def midpoint(n, x0, xn):
    # Calculate the integral of f(x) = sin(x)exp(-x/2) over the interval x = [x0,xn]
    f = lambda x : np.sin(x)*np.exp(-x/2)
    dx = (xn-x0)/n
    return dx * sum( f( np.linspace(x0+dx/2, xn-dx/2, n) ) )

x = [-1,2*np.pi]
n = [10,20,100,200,400,800,1600]

integrals = []
for n_i in n:
    integrals.append(midpoint(n_i, x[0], x[1]))

F = lambda x : -2/5 * np.exp(-x/2) * ( np.sin(x) + 2*np.cos(x) )
exact_integral = F(x[1]) - F(x[0])

#print((integrals-exact_integral)/exact_integral * 100)

plt.plot(n,integrals, marker='o', label='Numerical Integrations')
plt.axhline(exact_integral, color='r', label='Exact Integral')
plt.title("Value of numerical integrations using midpoint rule\n\
 as a function of n (the number of subintervals)")
plt.xlabel("n")
plt.ylabel("Numerical Integration")
plt.grid(True)
plt.legend()
plt.savefig("plot_func.pdf")
plt.show(block=False)
