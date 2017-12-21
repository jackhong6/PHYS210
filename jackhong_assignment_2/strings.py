# Define strings
hello = "Hello"
world = "World"
phys210 = "PHYS210"

# Combine the 3 strings
combined_str = hello + world + phys210

# Add three copies of "UBC" to the end of combined_str
cmb_str_3xUBC = combined_str + 3*"UBC"

# Make all characters in combined_str_3xUBC lower case
cmb_str_3xUBC = cmb_str_3xUBC.lower()

# Remove all occurences of the characters "o" and "l" and print combined_str_3xUBC
cmb_str_3xUBC = cmb_str_3xUBC.replace("o", "")
cmb_str_3xUBC = cmb_str_3xUBC.replace("l", "")
print(cmb_str_3xUBC)
