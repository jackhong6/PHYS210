# PHYS 210 Assignment 7, Part 2: Monte Carlo methods
# Jack Hong, 30935134
# September 29, 2016

import numpy as np

def unit_circle_area1(n):
    # Use the monte carlo method to calculate the area of a quarter of a circle
    # This function uses two arrays to store the x and y coordinates.
    x = np.random.random((n,))
    y = np.random.random((n,))
    count = 0
    for xi in x:
        for yi in y:
            if np.sqrt(xi**2 + yi**2) <= 1:
                count = count + 1
    return 4*count/n**2

def unit_circle_area2(n):
    # Use the monte carlo method to calculate the area of a quarter of a circle
    # This function does not use arrays.
    count = 0
    for i in range(0,int(n)):
        for j in range(0,int(n)):
            x = np.random.random()
            y = np.random.random()
            if np.sqrt(x**2 + y**2) <= 1:
                count = count + 1
    return 4*count/n**2

def test_monte_carlo():
    # Test if the monte carlo method returns a pi estimate within 10% of the true value of pi
    # consistently (100 times in a row)
    for n in range(1,1000): # n is the number of points to use for the monte carlo method
        passed = True
        for m in range(100): # try the monte carlo method 100 times
            pi_estimate = unit_circle_area1(n)
            if abs(pi_estimate-np.pi)/np.pi*100 > 10:  # if error of pi_estimate is greater than 10%
                passed = False                 #    then set passed to false and
                break                          #    try a bigger value of n
        if passed == True:
            return n  # return n if the pi estimate is with pi 100 times in a row

def test_monte_carlo_stats():
    trials = []
    for n in range(10): # run test_monte_carlo 10 times and store the result
        trials.append(test_monte_carlo())
    return trials

n = 100
pi1 = unit_circle_area1(n)
error1 = abs(pi1-np.pi)/np.pi*100
pi2 = unit_circle_area2(n)
error2 = abs(pi2-np.pi)/np.pi*100

print("unit_circle_area1: {}. Error is: {:.2f}%".format(pi1,error1))
print("unit_circle_area2: {}. Error is: {:.2f}%".format(pi2,error2))
print("True value of pi (approx): {}".format(np.pi))

print("\nPlease wait a few seconds. Calculating some statistics...")
stats = test_monte_carlo_stats()
print("The mean number of points needed to get an estimate of pi within 10% \n\
100 times in a row is: {} with a standard deviation of {}".format(np.mean(stats), np.std(stats)))
