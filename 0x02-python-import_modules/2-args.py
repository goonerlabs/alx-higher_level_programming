#!/usr/bin/python3
import sys


def print_args():
    args = sys.argv
    length = len(args) - 1

    if length == 0:
        print(f"{length} arguments.")
    elif length == 1:
        print(f"{length} argument:")
    else:
        print(f"{length} arguments:")
    for i in range(1, length  + 1):
        print(f"{i}: {args[i]}")


if __name__ == "__main__":
    print_args()
