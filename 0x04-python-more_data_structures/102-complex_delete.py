#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """A function that deletes keys with a specific value in a dictionary"""
    [a_dictionary.pop(key) for key, val in list(a_dictionary.items()) if val == value]
    return a_dictionary
