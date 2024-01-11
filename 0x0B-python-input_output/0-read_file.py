#!/usr/bin/python3
<<<<<<< HEAD
"""Task 0"""


def read_file(filename=""):
	"""Reads contents of a text file and print to stdout.

	Args:
	filename (str): name of file to be opened
	"""
	with open(filename, encoding='utf-8') as file:
		print(file.read(), end='')
=======
"""Read file task"""


def read_file(filename=""):
    """Reads contents of a text file and print to stdout.

    Args:
    filename (str): name of file to be opened
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
>>>>>>> 6c226157cef0e4ec56f82011c707ff73bb94f6d9
