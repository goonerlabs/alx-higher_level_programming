#!/usr/bin/python3
def weight_average(my_list=[]):
    if (not my_list):
        return 0
    sums = sum([i[0] * i[1] for i in my_list])
    weigths = sum([i[1] for i in my_list])
    return sums / weigths
