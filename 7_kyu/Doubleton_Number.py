"""
Reference: https://www.codewars.com//kata/604287495a72ae00131685c7
"""


def doubleton(num):
    while len(set(str(num + 1))) != 2:
        num += 1
    return num + 1


print(doubleton(120), 121)
print(doubleton(1234), 1311)
print(doubleton(10), 12)
print(doubleton(1), 10)
print(doubleton(111), 112)
