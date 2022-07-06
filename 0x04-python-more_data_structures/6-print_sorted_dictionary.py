#!/usr/bin/pyhton3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    for k in sorted(keys):
        print("{}: {}".format(k, a_dictionary[k]))
