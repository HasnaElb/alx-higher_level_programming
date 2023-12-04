#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace element of a list at a specific position."""
    if idx < 0 and idx > len(my_list) - 1:
        return my_list
    if my_list[idx]:
        my_list[idx] = element
    return my_list
