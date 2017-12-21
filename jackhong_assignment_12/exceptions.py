# PHYS 210 - Assignment 12, Question 1: Exception handling
# Jack Hong, 30935134
# October 19, 2016

def dictionary_lookup(fname, s1):
    # Return the word corresponding to s1 in the dictionary (same row)
    # Print error message instead of throwing exception if the file or word is not found.
    try:
        with open(fname) as f:
            lines = f.readlines()
            kv_pairs = []
            for line in lines:
                words = line.split()
                kv_pairs.append( (words[0], words[1]) )
            my_dict = dict(kv_pairs)
            return my_dict[s1]
    except KeyError as inst:
        print("Could not find key: ", inst)
    except IOError as inst:
        print(inst)

print( dictionary_lookup('dict_example.txt', 's1') ) # works; returns w1
print( dictionary_lookup('non_existant_file.txt', 's1') ) # file does not exist
print( dictionary_lookup('dict_example.txt', 'non_existant_key') ) # key does not exist
