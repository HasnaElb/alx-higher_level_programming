#!/usr/bin/python3

def best_score(a_dictionary):
    """A function that returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    result = list(a_dictionary.keys())[0]
    big = a_dictionary[result]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            result = k
    return (result)
