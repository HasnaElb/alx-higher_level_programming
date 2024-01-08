#!/usr/bin/python3
"""create a new class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square inherits of Rectangle"""

    def __init__(self, size):
        """
        Initialize a new square.
        Args:
        size (int): The width of the new rectangle.
        """

        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """provides printable representation of Rectangle object."""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
