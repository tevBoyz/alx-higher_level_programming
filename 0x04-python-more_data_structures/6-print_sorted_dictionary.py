#!/usr/bin/pyhton3
def print_sorted_dictionary(a_dictionary):
    for k in sorted(list(a_dictionary)):
        print("{}: {}".format(k, a_dictionary[k]))
