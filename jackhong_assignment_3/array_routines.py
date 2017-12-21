import numpy as np

# Question 1: Create an array with elements 0 to 9
a1 = np.array(range(0,10))
print(a1)

# Question 2: Create an array with elements x**2 for x = 0,1,...,9
a2 = a1**2
print(a2)

# Question 3: Take the sqrt of the array from the last question.
a3 = np.sqrt(a2)
print(a3)

# Question 4: Calculate the volume of spheres with radii r = 1,2,3,...,10
volume_of_spheres = 4 / 3 * np.pi * np.array(range(1,11))**3
print(volume_of_spheres)

# Question 5: Create a 1D array of size 12 with random numbers in the range 0 to 2pi
a4 = np.random.rand(12,) * 2 * np.pi
print(a4)

# Question 6: Calculate the sine of the numbers you created in Q5
a5 = np.sin(a4)
print(a5)
