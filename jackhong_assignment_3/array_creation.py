import numpy as np

# Question 1: Create a 1D array with 5 elements of your choice
array1 = np.array([1,2,3,4,5])
print(array1)

# Question 2: Create a 1D array with 3 single precision floating point numbers.
array2 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
print(array2)
# Show that this array has indeed the correct data type
print(array2.dtype)    # prints float32
print(type(array2[0])) # prints <class 'numpy.float32'>

# Question 3: Create an array with elements 0 to 500
array3 = np.array(range(0,501))
print(array3)

# Question 4:
print(array3[2])             # print element 3
print(array3[24])            # print element 25
print(array3[range(99,110)]) # print elements 100 to 110

# Question 5: Create a 1D array of size 10 filled with random numbers between 0 and 1
array4 = np.random.rand(10,)
print(array4)
