#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """A function that print a dictionary by ordered keys"""
    [print("{}: {}".format(k, a_dictionary[k])) for k in sorted(a_dictionary)]
