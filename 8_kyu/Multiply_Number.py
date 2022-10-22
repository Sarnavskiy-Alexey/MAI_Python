"""
Reference: https://www.codewars.com//kata/5708f682c69b48047b000e07
"""


def multiply(n):
    return n * 5 ** (len(str(abs(n))))

if __name__ == '__main__':
    print(multiply(7))
    print(multiply(15))
    print(multiply(15231))
    print(multiply(-15))
