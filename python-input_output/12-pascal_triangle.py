#!/usr/bin/python3
'''Module to define a function pascal_triangle'''


def pascal_triangle(n):
    '''
    Function that returns a list of lists of integers representing
    the Pascal's triangle of n.
    '''

    if n <= 0:
        return []

    res = [[1]]
    for i in range(1, n):  # ０行目は直接代入。1行目からloop
        tmp = []
        if i > 1:
            for j in range(1, i):  # index1から-1までloop
                tmp.append(res[i-1][j-1] + res[i-1][j])
        tmp.insert(0, 1)
        tmp.append(1)
        res.append(tmp)

    return res
