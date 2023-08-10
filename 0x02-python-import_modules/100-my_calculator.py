#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calc():
    av = sys.argv
    ac = len(av) - 1

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    funcs = {"+": add, "-": sub, "*": mul, "/": div}
    a = int(av[1])
    operator = av[2]
    b = int(av[3])

    if operator  not in funcs.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, funcs[operator](a, b)))

if __name__ == "__main__":
    calc()
