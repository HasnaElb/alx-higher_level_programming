#!/usr/bin/python3
"""Define an empty class"""


class BaseGeometry(object):
    """new class"""

    def area(self):
        """function for calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function for validate integer object"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
