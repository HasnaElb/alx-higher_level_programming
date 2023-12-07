#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """A function that replace or add key/value pairs
    in a dictionary"""
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
