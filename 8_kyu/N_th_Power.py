def index(array, n):
    """
    You are given an array with positive numbers and a non-negative number N. You should find the
    N-th power of the element in the array with the index N. If N is outside of the array, then
    return -1. Don't forget that the first element has the index 0.
    """
    return array[n] ** n if n < len(array) else -1


if __name__ == '__main__':
    print(index([1, 2, 3, 4], 4))
