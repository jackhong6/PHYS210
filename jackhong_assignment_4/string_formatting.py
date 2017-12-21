# Assignment 4, Part 2: Formatting
import numpy as np

# Question 1:
data = np.loadtxt('ludoarray.txt') # load the data from ludoarray.txt as a numpy array
row2 = data[1,:]   # Pick out row 2 from data
row3 = data[2,:]   # Pick out row 3 from data

# Old style string formatting
old_str_format = "Data-point number %d has values of x=%.2f and y=%.2f, with errors of %.3f and %.2f, respectively."
print(old_str_format % (row2[0],row2[1],row2[2],row2[3],row2[4]))
print(old_str_format % (row3[0],row3[1],row3[2],row3[3],row3[4]))


# Question 2:
# New style string Formatting
new_str_format = "Data-point number {:d} has values of x={:.2f} and y={:.2f}, with errors of {:.3f} and {:.2f}, respectively."
print(new_str_format.format(int(row2[0]),row2[1],row2[2],row2[3],row2[4]))
print(new_str_format.format(int(row3[0]),row3[1],row3[2],row3[3],row3[4]))

# Question 3:
username = "jackhong"
assignment_num = 4
fname = "string_formatting.py"
path = "~/{:s}_assignment_{:d}/{:s}".format(username,assignment_num,fname)
print(path)
