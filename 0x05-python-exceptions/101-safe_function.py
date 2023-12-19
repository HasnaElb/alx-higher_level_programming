#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    Safely calls a function with provided arguments and handles exceptions.

    Args:
        fct (callable): The callable object to be executed.
        *args: Variable number of arguments to be passed to the callable.

    Returns:
        Any: The result of the function if successful, None otherwise.
    """
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
