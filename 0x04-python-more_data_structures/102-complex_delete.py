#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """A function that deletes keys with a specific value in a dictionary"""
    while value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[key]
                break

    return (a_dictionary)
