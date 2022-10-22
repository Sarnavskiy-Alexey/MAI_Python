"""
Reference: https://www.codewars.com//kata/57be674b93687de78c0001d9
"""


def largest_power(N):
    i = -1
    while 3 ** (i + 1) < N:
        i += 1
    return i


print(largest_power(0), '==', -1)
print(largest_power(3), '==', 0)
print(largest_power(4), '==', 1)