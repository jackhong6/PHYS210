# PHYS 210 Assignment 9, Part 2: Numpy Arrays and Functions
# Jack Hong, 30935134
# October 7, 2016

import numpy as np
import sys

def my_sign(a):
    # Return a numpy array of signs: -1,0,1, where each position in the returned
    # array matches the position in a.
    # This function does not modify the original array.
    sign_array = np.copy(a)
    sign_array[a>0] = 1
    sign_array[a<0] = -1
    return sign_array

def main():
    # Test the my_sign function above
    test_array = np.array([[1,0,-1],[123,-123,0],[0, 456, -456]])
    sign_array = my_sign(test_array)
    print("Test array:\n {}".format(test_array))
    print("my_sign returned:\n {}".format(sign_array))
    while True:
        try:
            array = np.matrix(input("Enter an array to test my_sign (Ex. \"1,0 ; 0,1\"): "))
            print("Input:\n {}\n".format(array))
            print("my_sign returned:\n {}.".format(my_sign(array)))
        except KeyboardInterrupt:
            print("")
            sys.exit(0)
        except Exception as inst:
            print("Hmm... that didn't work because {:s}".format(str(inst).lower()))
            print("Please try again.")
            pass


if __name__ == "__main__":
    main()
