#!/usr/bin/python3
"""function that returns True if the object is an instance of,
or if the object is
an instance of a class that inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """
    returns True if a is instance of a_class else False
    """
    if isinstance(obj, a_class) or issubclass(a_class, type(obj)):
        return True
    else:
        return False
