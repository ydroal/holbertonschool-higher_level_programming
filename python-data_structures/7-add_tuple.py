#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    la = list(tuple_a)
    lb = list(tuple_b)

    if la == []:
        la = [0, 0]
    elif len(la) == 1:
        la.append(0)

    if lb == []:
        lb = [0, 0]
    elif len(lb) == 1:
        lb.append(0)

    a = la[0] + lb[0]
    b = la[1] + lb[1]
    return (a, b)
