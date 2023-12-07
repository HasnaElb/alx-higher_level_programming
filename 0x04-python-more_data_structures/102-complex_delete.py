#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """A function that deletes keys with a specific value in a dictionary"""
    a_list = list(a_dictionary.keys())
    for key in a_list:
        if a_dictionary[key] == value:
            del a_dictionary[key]
        return a_dictionary
