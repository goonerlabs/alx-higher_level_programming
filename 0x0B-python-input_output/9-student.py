#!/usr/bin/python3
"""A student class"""


class Student:
    """A class that represents students"""

    def __init__(self, first_name, last_name, age):
        """initializes an object of type student
        Args:
            first_name (str): the students first name
            last_name (str): the students last name
            age (int): the students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary representation of a student object"""
        return self.__dict__
