#!/usr/bin/pyhton3
def print_sorted_dictionary(a_dictionar):
    for k in sorted(list(a_dictionar.keys())):
        print("{}: {}".format(k, a_dictionar[k]))
