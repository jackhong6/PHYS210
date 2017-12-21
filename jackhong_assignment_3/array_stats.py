import numpy as np

# Create a 1D array of size 100 with numbers drawn uniformly from the interval [0,1)
a = np.random.random(100)
print(a)

# Calculate the mean of the elements of a
mean = np.sum(a) / a.size
# My calculated mean and the numpy mean agree. This is what I would expect.
print("My calculated mean: " + str(mean))
print("Numpy calculated mean: " + str(np.mean(a)))

# Calculate the variance of the elements of a
var = 1/(a.size - 1) * np.sum( (a - mean)**2 )
# My calculated variance and numpy variance are very slightly different.
# This is not what I expected, so numpy is calculating something a bit different.
print("My calculated variance: " + str(var))
print("Numpy calculated variance: " + str(np.var(a)))

# Calculate the standard deviation of the elements of a
std = np.sqrt(var)
# My calculated variance and numpy std are very slightly different.
# This is not what I expected, so numpy is calculating something a bit different.
print("My calculated standard deviation: " + str(std))
print("Numpy calculated standard deviation: " + str(np.std(a)))

print("The mean, variance, and standard deviations above are about what I would expect \n \
from a sample of uniformly distributed random numbers in the interval [0,1). \n \
My calculated mean and the numpy mean agree. This is exactly what I would expect. \n \
However, my calculated variance and standard deviation are slighty different from \n \
the numpy calculated values. From what I understand (explained to me by a TA), numpy \n \
uses a different formula from what was given in the lab: \n \
1/(a.size) * np.sum( (a - mean)**2 ) vs 1/(a.size - 1) * np.sum( (a - mean)**2 ). \n \
This hypothesis is verified below (note that the following numbers match the numpy values above): ")

var2 = 1/(a.size) * np.sum( (a - mean)**2 )
std2 = np.sqrt(var2)
print("Variance calculated by the presumed numpy formula: " + str(var2))
print("Std calculated by the presumed numpy formula: " + str(std2))

print("\n From this, I conclude that numpy.var and numpy.std are calculating something slightly different from \n \
\"the (unbiased) estimator for the sample variance and standard deviation\".")
