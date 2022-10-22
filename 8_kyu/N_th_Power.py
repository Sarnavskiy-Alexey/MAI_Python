def index(array, n):
    """
    Reference: https://www.codewars.com//kata/57d814e4950d8489720008db
    """
    return array[n] ** n if n < len(array) else -1


if __name__ == '__main__':
    print(index([1, 2, 3, 4], 4))
