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

    @property
    def size(self):
        """Get the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""

        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of an instance of a square"""

        return (self.__size * self.__size)

    def my_print(self):
        """Prints a representation of a square with the character #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
