#!/usr/bin/python3
"""new class inherits from of class list"""


class MyList(list):
    """define a new class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
