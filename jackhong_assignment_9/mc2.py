# PHYS 210 Assignment 9, Part 1: Monte Carlo II
# Jack Hong, 30935134
# October 6, 2016

import numpy as np
import matplotlib.pyplot as plt
import time

def unit_circle_area_loop(n):
    # Use the monte carlo method to calculate the area of a unit circle. (pi)
    # param n is the number of points to use.
    # This function uses for loops.
    x = np.random.random((n,))
    y = np.random.random((n,))
    count = 0
    for k in range(n):
            if np.sqrt(x[k]**2 + y[k]**2) < 1:
                count = count + 1
    return 4*count / n

def unit_circle_area_vec(n, plotfig=False):
    # Use the monte carlo method to calculate the area of a unit circle. (pi)
    # param n is the number of points to use.
    # This function does not use for loops.
    x = np.random.random((n,))
    y = np.random.random((n,))
    r = np.sqrt(x**2 + y**2)
    in_circle = r < 1
    not_in_circle = np.invert(in_circle)
    if plotfig:
        plt.figure();
        plt.scatter(x[in_circle], y[in_circle], marker='.', color='r')
        plt.scatter(x[not_in_circle], y[not_in_circle], marker='.', color='b')
        plt.xlim([0,1])
        plt.ylim([0,1])
        plt.savefig("mc_scatter_plot.pdf")
        plt.show(block=False)
    return 4 * sum(in_circle) / n

def main():
    n = int(1e6)
    start = time.time()
    vec_pi = unit_circle_area_vec(n)
    end = time.time()
    vec_time = end - start

    start = time.time()
    loop_pi = unit_circle_area_loop(n)
    end = time.time()
    loop_time = end - start

    print("The vectorized code ran in {}s and returned {}".format(vec_time,vec_pi))
    print("The iterative code ran in {}s and returned {}".format(loop_time,loop_pi))
    #loop_pi_est = unit_circle_area_loop(100)
    #print(loop_pi_est)



if __name__ == "__main__":
    main()
