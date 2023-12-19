#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Prints an integer with "{:d}".format().
    if a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        Value (int): The integer to print.

    Returns:
        if a ValueError occurs - False
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
