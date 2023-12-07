#!/usr/bin/python3
"""Function that reads a file"""


def read_file(filename=""):
    """reads a file and prints the contents to stdout
    Args:
        filename: (str) the name of the file to read
    """

    with open(filename) as f:
        for line in f:
            print(line, end="")
