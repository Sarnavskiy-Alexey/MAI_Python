"""
Reference: https://www.codewars.com//kata/57fafb6d2b5314c839000195
"""


def remove(s):
    l = s.split(' ')
    for el in l[::-1]:
        if el.count('!') == 1:
            l.remove(el)
    return str(" ".join(l))


if __name__ == '__main__':
    print(remove('Hi!'))
    print(remove('Hi!!!'))
    print(remove('!Hi'))
    print(remove('!Hi!'))
    print(remove('Hi! Hi!'))
    print(remove('!!!Hi !!hi!!! !hi'))
    print(remove('!Hi! ! !Hi!'))
