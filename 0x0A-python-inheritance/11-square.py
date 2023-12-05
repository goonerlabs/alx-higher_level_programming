#!/usr/bin/python3
"""Square class that inherits from the Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from the Rectangle class"""

    def __init__(self, size):
        """Initializes a new Square
        Args:
            size (int): size of the square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns a string representation of a square"""

        return "[Square] {}/{}".format(self.__size, self.__size)
