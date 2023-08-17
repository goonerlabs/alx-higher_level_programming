#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return 0

    num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    temp = 0
    res = 0

    for c in roman_string:
        if c not in num_dict:
            return 0
        temp_2 = num_dict[c]
        if temp_2 > temp:
            res += temp_2 - 2 * temp
        else:
            res += temp_2
        temp = temp_2
    return res
