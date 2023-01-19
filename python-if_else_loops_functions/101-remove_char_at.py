#!/usr/bin/python3
def remove_char_at(str, n):
    res = str[:n] + str[n+1:]
    return res
