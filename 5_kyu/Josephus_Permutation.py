"""
    Reference: https://www.codewars.com//kata/5550d638a99ddb113e0000a2
"""


def josephus(items ,k):
    counter = 0
    res = []

    while len(items):
        counter = (counter + k - 1) % len(items)
        res.append(items.pop(counter))
    return res
