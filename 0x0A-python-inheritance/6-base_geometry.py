#!/usr/bin/python3
"""Base class for all geometry classes"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
