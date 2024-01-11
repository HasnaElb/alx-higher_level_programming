#!/usr/bin/python3
"""define a new function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number
    of characters written. overwrites existing content.

    Args:
    filename (str): name of file to be opened. Default to "".
    text (str): string for add to file. Default to "".

    Returns:
    [int]: number of lines adds
    """
    # with w flag existing file automatically replaced
    with open(filename, mode='w', encoding='utf-8') as my_file:
        my_file.write(text)
        return len(text)
