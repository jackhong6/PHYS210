# PHYS 210 - Assignment 12, Question 2: Numerical Differentiation
# Jack Hong, 30935134
# October 19, 2016

import numpy as np
import matplotlib.pyplot as plt

def deriv(f, x, h=1e-5):
    # Return the approximate derivative of f at x using the step size h
    return (f(x+h) - f(x))/h

# =============================
x = np.linspace(0,10,100)

f = lambda x : np.sin(x) + 10*x
num_diff = deriv(f,x)

f_prime = lambda x : np.cos(x) + 10
ana_diff = f_prime(x)

# =============================
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(x, num_diff, color='r')
plt.title('Numerical Differentiation of f(x)=sin(x) + 10x')
plt.xlabel('x')
plt.ylabel("f'(x)")

plt.plot(x, ana_diff)
plt.title('Analytical Differentiation of f(x)=sin(x) + 10x')
plt.xlabel('x')
plt.ylabel('cos(x) + 10')

plt.subplot(2,1,2)
plt.plot(x, abs(num_diff - ana_diff)/ana_diff, color='m')
plt.title('Fractional Differences')
plt.savefig('derivative.pdf')
# ============================
plt.figure(2)
hs = np.linspace(1e-16, 1e-2, 1000)
mean_errors = []

for h in hs:
    errors = np.abs(deriv(f,x,h)-f_prime(x))
    mean_errors.append( np.mean(errors) )

plt.loglog(hs, mean_errors)  # Plot shows that optimal h is around 1e-5
plt.title('Log-Log Plot of Error vs h')
plt.xlabel('h')
plt.ylabel('Error')
plt.savefig('error_vs_h.pdf')
plt.show()
