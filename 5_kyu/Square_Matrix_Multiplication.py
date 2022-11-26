"""
    Reference: https://www.codewars.com//kata/5263a84ffcadb968b6000513
"""


def matrix_mult(a, b):
    res = [[0] * len(a) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(a[i])):
                res[i][j] += a[i][k] * b[k][j]

    return res
