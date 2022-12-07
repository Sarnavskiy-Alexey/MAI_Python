"""
Reference: https://www.codewars.com//kata/568f2d5762282da21d000011
"""


from itertools import permutations


def gta(limit, *args):
    numbers = []
    for x in args:
        numbers += [str(x)]

    base_list = []
    idx = 0
    while idx < limit:
        for num in numbers:
            if len(num) > idx and int(num[idx]) not in base_list and limit > len(base_list):
                base_list += [int(num[idx])]
        idx += 1

    return sum([sum([sum(item) for item in list(permutations(base_list, i))]) for i in range(1, limit + 1)])
