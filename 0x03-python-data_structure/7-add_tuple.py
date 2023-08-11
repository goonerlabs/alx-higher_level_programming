#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b, *_ = tuple_a + (0, 0, 0)
    c, d, *_ = tuple_b + (0, 0, 0)
    return (a + c, b + d)
