# PHYS 210: Assignment 6, Problem 2
# Jack Hong, 30935134
# Last Modified: September 27, 2016

def in_mandelbrot(c):
    # Check if c is in the mandelbrot set using iteration
    z = 0
    max_iter = 1000
    num_iter = 1
    while num_iter < max_iter:
        z = z**2 + c
        num_iter = num_iter + 1
        if abs(z) > 2:
            return False
    return True

def in_mandelbrot_recursive_helper(c, z, max_recursions):
    # Check if c is in the mandelbrot set using recursion.
    # Max for max_recursions is 975 for default stack depth
    if abs(z) > 2:
        return False
    if max_recursions == 0:
        return True
    return in_mandelbrot_recursive_helper(c,z**2+c, max_recursions-1)

def in_mandelbrot_recursive(c):
    return in_mandelbrot_recursive_helper(c, 0, 975)


# ---------------- TEST CODE --------------------
test = True # Set to True to run the test code below

def test_mandelbrot(c, expected):
    # Return True if and only if both in_mandelbrot and in_mandelbrot_recursive
    # return the expected result
    iter_result = in_mandelbrot(c)
    recur_result = in_mandelbrot_recursive(c)
    if iter_result == expected and recur_result == expected:
        return True
    else:
        print("TEST FAILED: in_mandelbrot({}) returned {}; in_mandelbrot_recursive({}) returned {}; expected {}"\
    .format(c, iter_result, c, recur_result, expected))
        return False

if test:
    in_set = [0, 1j, -1, -.65,-1.1,-1.75, -0.2+0.3j, 0.2-0.3j, -2] # Known to be in the Mandelbrot set
    not_in_set = [1, 2j, -2.1, 2, 1+1j, -8-0.55j, 0.5+0.7j, 0.8-1j] # Known to not be in the Mandelbrot set
    for k in range(0,len(in_set)):
        c = in_set[k]
        passed = test_mandelbrot(c, True)
        print("Test for {} {:s}".format(c, "passed" if passed else "failed"))
    for k in range(0,len(not_in_set)):
        c = not_in_set[k]
        passed = test_mandelbrot(c, False)
        print("Test for {} {:s}".format(c, "passed" if passed else "failed"))
