# PHYS 210, Assignment 11: Part 1 - Dictionaries
# Jack Hong, 30935134
# October 13, 2016

def concatenate(a,b,c):
    # Return a new dictionary by concatenating dictionaries a,b,c
    concat_dict = a.copy()
    concat_dict.update(b)
    concat_dict.update(c)
    return concat_dict

def exists(d,s):
    # Return True if the key s already exists in dictionary d.
    # Must be run using Python 3
    return s in d
