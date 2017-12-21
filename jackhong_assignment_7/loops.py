# PHYS 210 Assignment 7, Part 1: Loops
# Jack Hong, 30935134
# September 29, 2016

import math
import numpy as np

# -------------------- Question 1: Exercise 1 from ch. 7 -----------------------
def mysqrt(a):
    # Return the square root of a
    epsilon = 1e-15
    x = a
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y
    return x

def test_square_root():
    # Print out test results for mysqrt
    print("a   mysqrt(a)      math.sqrt(a)   diff")
    print("-   ---------      ------------   ----")
    for a in range(1,10):
        my_sqrt = mysqrt(a)
        math_sqrt = math.sqrt(a)
        print("{:.1f} {:.12f} {:.12f} {:0.6g}".format(a, my_sqrt, math_sqrt, abs(my_sqrt-math_sqrt) ))

test_square_root()

# --------------------- Question 2: Exercise 4 from ch.8 -----------------------
print("\nFor question 2, the behaviour of the functions are described in comments \
in the code.\n")

def any_lowercase1(s):
    # Return True if all cased characters in s are lowercase and there is at
    # least one cased character. False otherwise.
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    # Return True if all cased characters in s are lowercase and there is at
    # least one cased character. False otherwise. (Same as any_lowercase1)
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    # Return True if the last character is lowercase. False otherwise.
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    # CORRECT! Return True if there is at least one lowercase letter.
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    # Return True if all cased characters in s are lowercase and there is at
    # least one cased character. False otherwise. (Same as any_lowercase1 and any_lowercase2)
    for c in s:
        if not c.islower():
            return False
    return True

# ------------------------------ Question 3 ------------------------------------
def calculate_mean_var_stddev(fname):
    data = np.loadtxt(fname)
    ncol = 1
    for col in data.T:  # iterate over columns of data
        print("Col {:d} is {}".format(ncol, col))
        print("Mean of column {:d} is: {}".format(ncol,np.mean(col)))
        print("Variance of column {:d} is: {}".format(ncol,np.var(col)))
        print("Std dev of column {:d} is: {}\n".format(ncol,np.std(col)))
        ncol = ncol+1

calculate_mean_var_stddev("ludoarray.txt")
