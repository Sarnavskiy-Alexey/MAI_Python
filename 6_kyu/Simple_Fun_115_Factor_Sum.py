"""
    Reference: https://www.codewars.com//kata/589d2bf7dfdef0817e0001aa
"""

def factor_sum(n):
    res = n
    nn = n
    s = 0
    i = 2
    while i <= (int(n / 2) + 1) and i <= nn:
        if nn % i:
            i += 1
        else:
            nn //= i
            s += i
    if s == 4:
        return s
    if s != 0:
        res = factor_sum(s)
    return res


if __name__ == '__main__':
    print(factor_sum(24), 5)
    print(factor_sum(35), 7)
    print(factor_sum(156), 5)
    print(factor_sum(4), 4)
    print(factor_sum(31), 31)
