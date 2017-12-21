# Assignment 4, Part 1: Reading files
import numpy as np
data = np.loadtxt('ludoarray.txt') # load the data from ludoarray.txt as a numpy array
print("The size of the array is %d x %d" % (data.shape[0],data.shape[1]))

col2_mean = np.mean(data[:,1]) # Calculate the mean of the 2nd column
col3_var = np.var(data[:,2])   # Calculate the variance of the 3rd column
print("The mean of column 2 is: {}".format(col2_mean))
print("The variance of column 3 is: {}".format(col3_var))

f = open('reading_files.py', 'r')
line1 = f.readline();
line2 = f.readline();
line3 = f.readline();
print("The first 3 lines of code are: \n{}{}{}".format(line1,line2,line3))
f.close()
