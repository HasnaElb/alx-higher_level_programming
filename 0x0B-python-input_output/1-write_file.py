#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number
    of characters written. overwrites existing content.

    Args:
    filename (str): name of file to be opened
    text (str): chars to be written
    """
    # with w flag existing file automatically replaced
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
