#!/usr/bin/python3
"""list class"""


class MyList(list):
    """my personal list class"""
    def print_sorted(self):
        """ prints a sorted list """
        print(sorted(self))
