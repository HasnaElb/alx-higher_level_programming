#!/usr/bin/python3
"""create a new class"""


class MyInt(int):
    """Class MyInt rebel"""

    def __init__(self, valor):
        """initialize var valor"""
        self.valor = valor

    def __eq__(self, other):
        """__eq__ represent a == b"""
        return self.valor != other

    def __ne__(self, other):
        """__ne__ represent a != b or a <> b"""
        return self.valor == other
