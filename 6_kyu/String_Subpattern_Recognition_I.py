"""
    Reference: https://www.codewars.com//kata/5a49f074b3bfa89b4c00002b
"""


def has_subpattern(string):
    l = find_all_devs(len(string))
    if len(string) > 1:
        for n in l:
            s = string.replace(string[:n], '')
            if not (len(s)):
                return True

    return False


def find_all_devs(s_length):
    if s_length <= 1:
        return [1]
    else:
        return [i for i in range(1, s_length // 2 + 1) if s_length % i == 0]