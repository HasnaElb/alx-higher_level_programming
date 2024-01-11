#!/usr/bin/python3
"""Task 0"""


def read_file(filename=""):
	"""Reads contents of a text file and print to stdout.

	Args:
	filename (str): name of file to be opened
	"""
	with open(filename, encoding='utf-8') as file:
		print(file.read(), end='')
