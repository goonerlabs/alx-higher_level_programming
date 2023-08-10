#!/usr/bin/python3
import sys


def print_args():
    args = sys.argv
    length = len(args) - 1

    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments:" .format(length))
    for i in range(1, length + 1):
        print("{}: {}".format(i, args[i]))


if __name__ == "__main__":
    print_args()
