import numpy as np

def mean(np_array):
    return np.sum(np_array) / np_array.size

def variance(np_array):
    m = mean(np_array)
    return 1/(np_array.size - 1) * np.sum( (np_array - m)**2 )

def std_dev(np_array):
    return np.sqrt(variance(np_array))
