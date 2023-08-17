#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    temp = a_dictionary.copy()
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == value:
                del temp[k]
        return temp
