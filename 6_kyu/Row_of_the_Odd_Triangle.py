"""
    Reference: https://www.codewars.com//kata/5d5a7525207a674b71aa25b5
"""


def odd_row(n):
    return [n * (n - 1) + 1 + 2 * i for i in range(n)]
