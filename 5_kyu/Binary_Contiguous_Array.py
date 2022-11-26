"""
    Reference: https://www.codewars.com//kata/60aa29e3639df90049ddf73d
"""


def binarray(s) -> int:
    d1 = {0: 0}
    d2 = {}
    prefix_sum = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        # образуем префиксную сумму
        prefix_sum[i] += prefix_sum[i - 1] + (1 if s[i - 1] else -1)

        # заполняем словари
        if prefix_sum[i] in d1:
            d2.update({prefix_sum[i]: i})
        else:
            d1.update({prefix_sum[i]: i})
    max_n = 0
    if not len(d2):
        return max_n

    for i in range(-len(s) - 1, len(s) + 1):
        if d2.get(i):
            max_n = d2.get(i) - d1.get(i) if d2.get(i) - d1.get(i) > max_n else max_n

    return max_n
