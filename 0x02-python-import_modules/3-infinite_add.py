#!/usr/bin/python3
import sys


def infinite_add():
    args = sys.argv
    res = 0
    for i in range(1, len(args)):
        res += int(args[i])
    return res


if __name__ == "__main__":
    print(f"{infinite_add()}")
