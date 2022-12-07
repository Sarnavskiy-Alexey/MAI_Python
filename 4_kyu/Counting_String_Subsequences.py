"""
    Reference: https://www.codewars.com//kata/52f7892a747862fc9a0009a6
"""


def rec_foo(l, idx=-1):
    s = 0
    if len(l) > 1:
        for i in range(len(l[0])):
            if idx < l[0][i]:
                s += rec_foo(l[1:], l[0][i])
        return s
    else:
        for x in l[0]:
            if idx < x:
                s += 1
        return s


def count_subsequences(a, b):
    d = {c: [] for c in a}
    for idx, val in enumerate(b):
        if val in d:
            d[val] += [idx]

    l = []
    for c in a:
        l += [d[c]]

    return rec_foo(l)
