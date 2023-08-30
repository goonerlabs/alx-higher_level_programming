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

    def __eq__(self, square):
        """Returns True if the areas of both squares are equal"""

        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")
        return (self.area() == square.area())

    def __ne__(self, square):
        """Returns True if the areas of both squares are not equal"""

        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")
        return (self.area() != square.area())

    def __gt__(self, square):
        """Returns True if the area of the first square is
        greater than the area of the second square
        """
        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")
        return (self.area() > square.area())

    def __lt__(self, square):
        """Returns True if the area of the first square is
        less than the area of the second square
        """
        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")
        return (self.area() < square.area())

    def __ge__(self, square):
        """Returns True if the area of the first square is
        greater than or equal to the area of the second square
        """
        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")

        return (self.area() >= square.area())

    def __le__(self, square):
        """Returns True if the area of the first square is
        less than or equal to the area of the second square
        """
        if ((not isinstance(square, Square)):
            raise TypeError("argument must be an instance of Square")
        return (self.area() <= square.area())
