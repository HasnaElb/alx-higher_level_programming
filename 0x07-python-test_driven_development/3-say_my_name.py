#!/usr/bin/python3
"""Function that prints my name
@first_name and last_name must be strings
Return: only print arg in stdout
"""


def say_my_name(first_name, last_name=""):
    """
    function for say name givend in parameters
    """

    if first_name:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        elif type(last_name) is not str:
            raise TypeError("last_name must be a string")
        else:
            print("My name is {} {}".format(first_name, last_name))
