#!/usr/bin/python3
def uppercase(str):
    for i in str:
        uc = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            uc = uc - 32
        print('{:c}'.format(uc), end='')
    print()
