#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bs = max(a_dictionary.values())
    k_bs = ''
    for k, v in a_dictionary.items():
        if v == bs:
            k_bs = k_bs + k
    return k_bs
