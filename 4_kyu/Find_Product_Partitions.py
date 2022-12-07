"""
    Reference: https://www.codewars.com//kata/571dd22c2b97f2ce400010d4
"""

from itertools import combinations


def find_simples(n):
    l = []
    counter = 2
    while n > 1:
        if n % counter:
            counter += 1
        else:
            l += [counter]
            n //= counter
    return l


def find_mult_combinations(el):
    s = set()
    l = list(el).copy()
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            el_2 = l.copy()
            el_2[i] = l[i] * l[j]
            el_2.pop(j)
            s.add(tuple(sorted(el_2, reverse=True)))
            s.update(find_mult_combinations(tuple(el_2)))
    return s


def find_all_combinations(l):
    combos = set()
    comb = set()
    for i in range(len(l) - 1, 1, -1):
        combos.update(set(combinations(l, i)))

    for el in combos:
        s = find_mult_combinations(el)
        comb.update(s)
    combos.update(comb)
    return combos


def calculate_score(l):
    s = 0
    for el in set(l):
        s += el ** l.count(el)
    s *= len(l)
    return s


def find_spec_prod_part(n, com):
    l = find_simples(n)
    combos = set()
    combos_2 = set()
    if len(l) == 1:
        return 'It is a prime number'
    elif len(l) == 2:
        return [sorted(l, reverse=True), calculate_score(l)]
    combos = find_all_combinations(l)

    for el in combos:
        num = n
        l = []
        if type(el) == int:
            num //= el
            l += [el]
        else:
            for item in el:
                num //= item
                l += [item]
        combos_2.add(tuple(sorted(l + [num], reverse=True)))

    score = -1
    prod_partition = []
    for item in combos_2:
        calc = calculate_score(item)
        if com == 'max':
            if score < calc:
                score = calc
                prod_partition = list(item)
        elif com == 'min':
            if score > calc or score == -1:
                score = calc
                prod_partition = list(item)

    return [prod_partition, score]
