"""
    Reference: https://www.codewars.com//kata/599688d0e2800dda4e0001b0
"""


def find_num(n):
    l = [0]
    min_not_in = 1
    for i in range(1, n + 1):
        while min_not_in in l: min_not_in += 1
        next = min_not_in

        while next not in l:
            flag = True
            for el in str(next):
                flag = flag and (el not in str(l[-1]))
            if (next not in l) and flag:
                l.append(next)
            else:
                next += 1
                while next in l: next += 1

    return l[-1]
