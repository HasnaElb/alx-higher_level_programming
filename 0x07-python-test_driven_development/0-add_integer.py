#!/usr/bin/python3
"""
function for add two number int
@a & @b: must be integers or floats
Return: add by a and b
"""


def add_integer(a, b=98):
    """function for add number"""
    if a and b:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        elif not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        else:
            if type(a) is float:
                return int(a) + b
            elif type(b) is float:
                return a + int(b)
            else:
                return a + b
