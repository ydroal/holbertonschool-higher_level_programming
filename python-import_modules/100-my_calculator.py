#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    len = len(argv)
    op = ['+', '-', '*', '/']

    if len != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if not argv[2] in op:
        print(
            'Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    res = 0
    if argv[2] == op[0]:
        res = a + b
    elif argv[2] == op[1]:
        res = a - b
    elif argv[2] == op[2]:
        res = a * b
    elif argv[2] == op[3]:
        res = a / b

    print('{} {} {} = {}'.format(a, argv[2], b, res))
    exit
