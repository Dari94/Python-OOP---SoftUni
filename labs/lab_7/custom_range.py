class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current_num = self.start
        self.start += 1
        return current_num


one_to_ten = custom_range(20, 30)
for num in one_to_ten:
    print(num)
