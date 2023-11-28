#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle. """
        result = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            result = 0
        return result

    def __str__(self):
        """Return the str representation of the Rectangle
        represented by the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        res = []
        for i in range(self.__height):
            for j in range(self.__width):
                res.append("#")
            if i != self.__height - 1:
                res.append("\n")
        return ("".join(res))

    def __repr__(self):
        """Return the repr representation of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a Rectangle object is deleted."""
        print("Bye rectangle...")
