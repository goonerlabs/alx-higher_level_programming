#!/usr/bin/python3


""" Python class that does exactly the same as the Python bytecode """


import math


class MagicClass:
    """ a class that represents a circle shape """

    def __init__(self, radius=0):
        """ constructor """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ returns the area of the circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns the circumference of the circle """
        return (2 * math.pi * self.__radius)
