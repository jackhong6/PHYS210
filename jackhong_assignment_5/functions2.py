import numpy as np
import stats

# Load the column at the ith column, at the i-1 index
def load_col(fname, i):
    return np.loadtxt(fname, usecols=(i-1,))

y = load_col("ludoarray.txt", 3)
print("Column 3 (y) is: {}".format(y))

# Calculate the mean, variance, and std_dev of y
mean = stats.mean(y)
variance = stats.variance(y)
std_dev = stats.std_dev(y)

# Print the result of the calculations
print("The mean of y is {:f} \nThe variance of y is {:f} \nThe std deviation of \
y is {:f}".format(mean,variance,std_dev))
