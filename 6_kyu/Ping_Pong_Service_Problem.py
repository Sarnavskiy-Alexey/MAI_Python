"""
    Reference: https://www.codewars.com//kata/544bdc2ec29fb3456e00064a
"""


def service(score):
    pl_1 = int(score[:score.find(':')])
    pl_2 = int(score[score.find(':') + 1:])

    if pl_1 + pl_2 < 40:
        return "second" if ((pl_1 + pl_2) // 5) % 2 else "first"
    else:
        return "second" if ((pl_1 + pl_2 - 40) // 2) % 2 else "first"
