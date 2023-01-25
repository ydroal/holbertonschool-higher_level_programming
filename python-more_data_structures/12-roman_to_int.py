#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    convert = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lengs = len(roman_string)
    res = convert[roman_string[lengs - 1]]
    if lengs == 1:
        return res
    else:
        for i in range(lengs - 1, 0, -1):
            value1 = convert[roman_string[i]]
            value2 = convert[roman_string[i - 1]]
            if value1 > value2:
                res -= value2
            else:
                res += value2
        return res
