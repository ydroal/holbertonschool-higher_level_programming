#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    len = len(sys.argv)
    op = ['+', '-', '*', '/']

    if len != 4:
        sys.stderr.write('Usage: ./100-my_calculator.py <a> <operator> <b>\n')
        exit(1)

    if not sys.argv[2] in op:
        sys.stderr.write(
            'Unknown operator. Available operators: +, -, * and /\n')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    res = 0
    if sys.argv[2] == op[0]:
        res = a + b
    elif sys.argv[2] == op[1]:
        res = a - b
    elif sys.argv[2] == op[2]:
        res = a * b
    elif sys.argv[2] == op[3]:
        res = a / b

    print('{} {} {} = {}'.format(a, sys.argv[2], b, res))
    exit
