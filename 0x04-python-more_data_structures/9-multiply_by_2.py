#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """A function that a new dictionary with all values multipled by 2"""
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary.update({key: (value * 2)})
    return new_dictionary
