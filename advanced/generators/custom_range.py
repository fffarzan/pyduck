class ARange(): # The class is both the iterable and the iterator
    curr = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # In Python, an object becomes iterable if it has a method __iter__.
    # __iter__ tells to use this same object as the iterator.
    def __iter__(self):
        # we return self because this class holds the state (curr, last) and
        # performs iteration itself.
        return self

    def __next__(self):
        if self.curr < self.last:
            num = self.curr
            self.curr += 1
            return num

        raise StopIteration

a_range = ARange(0, 10)
for i in a_range:
    print(i)
