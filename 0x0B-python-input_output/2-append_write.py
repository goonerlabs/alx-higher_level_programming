#!/usr/bin/python3
"""utility function to append text to a file"""


def append_write(filename="", text=""):
    """appends text to filename
    Args:
        filename (str): the file to write to
        text (str): the text to append to filename
    Returns:
        the number of chars written
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
