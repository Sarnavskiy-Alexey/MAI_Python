"""
    Reference: https://www.codewars.com//kata/5603a9585480c94bd5000073
"""


def sum_dif_rev(n):
    counter = 0
    number = 11
    while counter < n:
        number += 1
        if number % 10:
            rev_n = int(str(number)[::-1])
            if (number - rev_n) and (number + rev_n) % (number - rev_n) == 0:
                counter += 1

    return number
