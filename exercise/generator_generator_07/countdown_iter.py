class countdown_iterator:
    def __init__(self,count):
        self.count = count
        self.iterator = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator < 0:
            raise StopIteration
        temp = self.iterator
        self.iterator -= 1
        return temp



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")


