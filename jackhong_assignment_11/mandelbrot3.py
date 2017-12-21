# # PHYS 210, Assignment 11: Part 3 - Mandelbrot III
# Jack Hong, 30935134
# October 13, 2016

import numpy as np
import matplotlib.pyplot as plt

def in_mandelbrot(c):
    # Return the number of iterations needed for c to diverge from the Mandelbrot formula.
    # c is a single complex number (not an array)
    z = 0
    max_iter = 100
    count = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return count
        z = z**2 + c
        count += 1
    return count

def mandelbrot_set(c, max_iter):
    # Array of complex num, int -> Array of int
    # Return number of iterations necessary for z_n to diverge.
    # Note: c is a numpy array
    z = np.zeros(c.shape)
    n2div = np.full(c.shape, max_iter)
    for n in range(max_iter):
        diverged = np.where(np.logical_and(abs(z) > 2, n2div == max_iter), z)
        n2div[diverged] = n
        z = z**2 + c if abs(z) < 2 else 2
    return n2div

def plot_mandelbrot_set_high_res1():
    # Plot high resolution image of the mandelbrot set.
    res = 1000
    max_iter = 100
    a = np.array(np.linspace(-2.5, 1, res))
    b = np.array(np.linspace(-1.5, 1.5, res))
    a,b = np.array(np.meshgrid(a,b))

    n2div = mandelbrot_set(a + 1j*b, max_iter)
    plt.figure()
    plt.imshow(np.log(n2div), cmap='viridis')
    plt.savefig('mandelbrot_highres_1.pdf')

def plot_mandelbrot_set_high_res2():
    # Plot high resolution image of the mandelbrot set.
    res = 1000
    max_iter = 100
    a = np.array(np.linspace(0, -1, res))
    b = np.array(np.linspace(-1, 0, res))
    a,b = np.array(np.meshgrid(a,b))

    n2div = mandelbrot_set(a + 1j*b, max_iter)
    plt.figure()
    plt.imshow(np.log(n2div), cmap='viridis')
    plt.savefig('mandelbrot_highres_2.pdf')

def plot_mandelbrot_set_low_res():
    # Plot low resolution image of the mandelbrot set.
    res = 100
    a = np.array(np.linspace(-2.5, 1, res))
    b = np.array(np.linspace(-1.5, 1.5, res))
    a,b = np.array(np.meshgrid(a,b))
    n2div = np.zeros( (res,res) )

    for x in range(res):
        for y in range(res):
            n2div[x,y] = in_mandelbrot(a[x,y]+1j*b[x,y])
    plt.figure()
    plt.imshow(n2div)
    plt.savefig('mandelbrot_lowres.pdf')

def main():
    plot_mandelbrot_set_low_res()
    plot_mandelbrot_set_high_res1()
    plot_mandelbrot_set_high_res2()
    plt.show()

if __name__ == "__main__":
    main()
