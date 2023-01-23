#!/usr/bin/python3


def multiple_returns(sentence):
    if not sentence:
        return (0, None)

    else:
        lengs = len(sentence)
        c = sentence[0]
        return (lengs, c)
