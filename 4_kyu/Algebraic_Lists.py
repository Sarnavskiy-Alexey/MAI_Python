"""
Reference: https://www.codewars.com//kata/529a92d9aba78c356b000353
"""


class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def to_array(self):
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr):
        # TODO: convert a Python list to an algebraic list.
        return cls(arr[0], cls.from_array(arr[1:])) if len(arr) > 1 else cls(arr[0], None) if len(arr) == 1 else None

    def filter(self, fn):
        # TODO: construct new algebraic list containing only elements
        #      that satisfy the predicate.
        return self.from_array(list(filter(fn, self.to_array())))

    def map(self, fn):
        # TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
        return self.from_array(list(map(fn, self.to_array())))


if __name__ == '__main__':
    print(Cons.from_array([]), '==', None)
    print(Cons.from_array([1, 2, 3, 4, 5]).to_array(), '==', [1, 2, 3, 4, 5])
    print(Cons.from_array([1, 2, 3, 4, 5]).filter(lambda n: n > 3).to_array(), '==', [4, 5])
    print(Cons.from_array([1, 2, 3, 4, 5]).filter(lambda n: n > 5), '==', None)
    print(Cons.from_array(["1", "2", "3", "4", "5"]).map(int).to_array(), [1, 2, 3, 4, 5])
    print(Cons.from_array([1,2,3,4,5]).filter(lambda n: n % 2 == 0).map(str).to_array(), '==', ["2", "4"])
