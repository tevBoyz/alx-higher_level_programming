#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = None
    for k in a_dictionary:
        if best is None:
            best = k
        else:
            if a_dictionary[k] > a_dictionary[best]:
                best = k
    return best
