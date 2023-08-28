#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    res = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        res = False
    return res
