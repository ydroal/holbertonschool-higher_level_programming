#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        res = number % 10
    else:
        res = (number * -1) % 10
    print(res, end='')
    return res
