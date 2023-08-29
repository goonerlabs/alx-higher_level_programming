#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """This class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of a square.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Gets the position attribute of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute of the square.
        Args: value (tuple): The position of the square. Defaults to (0, 0).
        Raises: TypeError: If value is not a tuple 2 elements.
            or if the its first or second element is not an integer
            or is negative.
        """
        if ((not isinstance(value, tuple)) or len(value) != 2 or
                (not isinstance(value[0], int)) or
            (not isinstance(value[1], int)) or
                (value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of an instance of a square"""

        return (self.__size * self.__size)

    def my_print(self):
        """Prints a representation of a square with the character #,
        at the poistion of the square, and with the size of the square
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """Returns a string representation of a square"""
        
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print()
        return ""
