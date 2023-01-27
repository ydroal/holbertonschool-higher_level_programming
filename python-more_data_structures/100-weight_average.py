#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    dividend = 0
    divisor = 0
    for i in range(len(my_list)):
        a, b = my_list[i]
        dividend += a * b
        divisor += b
    res = dividend / divisor
    return res
