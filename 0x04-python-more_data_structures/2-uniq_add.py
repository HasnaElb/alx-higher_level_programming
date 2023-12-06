#!/usr/bin/python3

def uniq_add(my_list=[]):
    """A function that add all unique integers in a list
    (once for each integers)"""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
