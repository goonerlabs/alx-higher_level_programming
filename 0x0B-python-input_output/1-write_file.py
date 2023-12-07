#!/usr/bin/python3
"""a utility function to write to a file"""


def write_file(filename="", text=""):
    """writes text into filename
    Args:
        text (str): the text to write into the file
        filename (str): the file to be written to
    Returns:
        the number of chars written
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
