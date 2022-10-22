def derive(coefficient, exponent):
    """
    Reference: https://www.codewars.com//kata/5963c18ecb97be020b0000a2
    """
    return str(coefficient * exponent) + 'x^' + str(exponent - 1)


if __name__ == '__main__':
    print(derive(7, 8))
