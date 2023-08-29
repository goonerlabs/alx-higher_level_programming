#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """Initializes an instance of a square.

        Args:
            size (int): The size of the square. Defaults to 0.
        """

        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
