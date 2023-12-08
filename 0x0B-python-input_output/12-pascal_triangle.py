#!/usr/bin/python3
"""function that creates a pascal triangle"""


def pascal_triangle(n):
    """function that creates a pascal triangle of n rows
    Args:
        n (int): the number of rows
    Returns:
        list of lists of integers
    """
    if n <= 0:
        return []

    res = []

    for i in range(n):
        row = [1]

        for j in range(1, i):
            temp = row[j - 1] * (i - j + 1) // j
            row.append(temp)

        if i > 0:
            row.append(1)

        res.append(row)

    return res
