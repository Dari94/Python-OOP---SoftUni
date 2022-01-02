def squares(n):
    num = 1
    while num <= n:
        yield num ** 2
        num += 1


class squares_iter:
    def __init__(self, n):
        self.n = n
        self.current_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num <= self.n:
            temp = self.current_num
            self.current_num += 1
            return temp ** 2
        raise StopIteration


def squares_3(n):
    return (x ** 2 for x in range(1, n + 1))


print(list(squares(5)))
print(list(squares_iter(5)))
print(list(squares_3(5)))
