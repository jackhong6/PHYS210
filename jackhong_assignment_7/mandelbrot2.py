def in_mandelbrot(c):
    # Check if c is in the mandelbrot set using iteration
    z = 0
    max_iter = 100
    for n in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return False # no need to use break
    return True

# ---------------- TEST CODE --------------------
test = True # Set to True to run the test code below

def test_mandelbrot(c, expected):
    # Return True if and only if both in_mandelbrot and in_mandelbrot_recursive
    # return the expected result
    iter_result = in_mandelbrot(c)
    if iter_result == expected:
        return True
    else:
        print("TEST FAILED: in_mandelbrot({}) returned {}; expected {}"\
    .format(c, iter_result, expected))
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
