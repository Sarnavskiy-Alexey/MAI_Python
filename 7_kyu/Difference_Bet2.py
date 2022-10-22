"""
Reference: https://www.codewars.com//kata/594093784aafb857f0000122
"""


def diff(a, b):
    c, d = a.copy(), b.copy()
    for el in a[::-1]:
        if el in b:
            c.remove(el)
    for el in b[::-1]:
        if el in a:
            d.remove(el)

    e = list(set(c + d))
    e.sort()
    return e


if __name__ == '__main__':
    print(diff(['a', 'b'], ['a', 'b']))
    print(diff([], ['a', 'b']))
    print(diff(['x', '1', 'i', 'e', 'r', '1', 'a', 'f', '7', 'x'], ['l', 'j', 'j', 'b', 'a', 'r', 'e', 'e', 'f', 'f']))
