# PHYS 210, Assignment 10: Part 1, Lists and Tuples I
# Jack Hong, 30935134
# October 12, 2016

def list2tupleends(t):
    # Return the first and last elements of the given list of numbers, t.
    # If t is empty, return nothing. If t contains only one element,
    # return a tuple containing two of that element.
    if len(t) == 0:
        return
    else:
        return (t[0], t[len(t)-1])

def noduplicates(t):
    # Return a new list containing the elements of t without duplicates.
    no_dup_list = []
    for item in t:
        if item not in no_dup_list:
            no_dup_list.append(item)
    return no_dup_list

def palindrome(s):
    # Return True if s is a palindrome.
    return str(s).lower() == str(s).lower()[::-1]

def lessthanten(t):
    # Return a new list containing all elements smaller than 10 with no duplicates.
    less_than_10 = []
    for n in t:
        if n < 10 and n not in less_than_10:
            less_than_10.append(n)
    return less_than_10

def truncate(t):
    # Modify t in place by removing the first and last elements. Return NoneType.
    # If t is empty, do nothing and return.
    if len(t) == 0:
        return
    elif len(t) == 1:
        del t[0]
    else:
        del t[0]
        del t[len(t)-1]
