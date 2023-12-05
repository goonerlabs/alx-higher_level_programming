#!/usr/bin/python3
"""Implemetation of rebel integer class"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override != operator with == behavior"""
        return super().__eq__(value)
