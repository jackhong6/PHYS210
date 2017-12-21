# PHYS 210: Assignment 6, Problem 1
# Jack Hong, 30935134
# Last Modified: September 27, 2016

import time

# ----------------------Ch.5, Exercise 1 ------------------
# Script that prints out the current time of day in (hh:mm:ss) format
# and the number of days since UNIX epoch
current_time = time.time()           # seconds since 1 January 1970
hrs = int((current_time/3600) % 24)
mins = int((current_time/60) % 60)
s = int(current_time % 60)
days = int(current_time / 86400)

print("The current time is (hh:mm:ss) {:02d}:{:02d}:{:02d} UTC".format(hrs,mins,s));
print("It has been {:d} days since 1 January 1970".format(days))

# ---------------------- Ch.5, Exercise 2 ------------------
print("\nFunctions for exercise 2 have been defined. If running in iPython, \n\
call check_fermat_prompt() to run.")

def check_fermat(a,b,c,n):
    # Check if Fermat's last theorem is refuted by the given values
    # and prints the result. Returns nothing.
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def check_fermat_prompt():
    # Prompt the user for values of a,b,c,n to check if Fermat's last theorem holds.
    print("This program checks if the values entered refute Fermat's last theorem.")
    print("Fermat's last theorem is: a**n + b**n != c**n for n>2")
    a = int(input("Enter a number for a: "))
    b = int(input("Enter a number for b: "))
    c = int(input("Enter a number for c: "))
    n = int(input("Enter a number for n: "))
    check_fermat(a,b,c,n)

# ----------------- Ch.5, Exercise 3 ---------------------
print("\nFunctions for exercise 3 have been defined. If running in iPython, \n\
call is_triangle_prompt() to run.")

def is_triangle(s1,s2,s3):
    # Print "No" if a triangle cannot be formed with sides of length s1,s2,s3,
    # i.e. if any of the three lengths is greater than the sum of the other two
    # Print "Yes" otherwise (including if the sum of two lengths equal the third).
    if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
        print("No")
    else:
        print("Yes")

def is_triangle_prompt():
    print("This program checks if a triangle can be formed with the given side lengths.")
    print("The program will print 'Yes' even for degenerate triangles.")
    s1 = float(input("Enter a side length: "))
    s2 = float(input("Enter another side length: "))
    s3 = float(input("Enter yet another side length: "))
    is_triangle(s1,s2,s3)

# ----------------- Ch. 6, Exercise 4 -------------------
print("\nThe function for exercise 4 has been defined. If running in iPython, \n\
call is_power(a,b) to run.")

def is_power(a,b):
    # Return True if a is a power of b. Return False otherwise.
    # Does not handle negative powers. (Always returns False for a < 1)
    # Does not handle fractional powers.
    if a == 1:
        return True
    else:
        return a % b == 0 and is_power(a/b, b)
