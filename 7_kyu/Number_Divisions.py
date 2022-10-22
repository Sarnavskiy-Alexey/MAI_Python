"""
Reference: https://www.codewars.com//kata/5913152be0b295cf99000001
"""


def divisions(n, divisor):
    counter = 0
    while n >= divisor:
        n = n // divisor
        counter += 1
    return counter


print(divisions(6, 2), '==', 2)
print(divisions(100, 2), '==', 6)
print(divisions(2450, 5), '==', 4)
print(divisions(9999, 3), '==', 8)
print(divisions(2, 3), '==', 0)
print(divisions(5, 5), '==', 1)
