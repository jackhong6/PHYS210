# Assignment 4, Part 3: Writing files
import numpy as np

# Question 1:
data = np.loadtxt('ludoarray.txt') # load the data from ludoarray.txt as a numpy array
col2_mean = np.mean(data[:,1]) # Calculate the mean of the 2nd column
col3_var = np.var(data[:,2])   # Calculate the variance of the 3rd column

# Write results to file stats.txt
f = open('stats.txt', 'w')
f.write("Mean[x] = {:f}\nVar[y] = {:f}".format(col2_mean, col3_var))
f.close

new_data = data
new_data[:,1] = 10 * new_data[:,1] # multiply the x column by 10
np.savetxt('data_new.txt', new_data, fmt='%d %.1f %.2f %.3f %.2f')
