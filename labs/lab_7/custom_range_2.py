class custom_range:
    def __init__(self, start, end, step=None):
        self.start = start
        self.end = end
        self.step = step
        self.counter = 0
        self.increment = step
        if step and step < 0:
            self.start, self.end = self.end, self.start
            self.increment = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.increment < 0:
            if self.start >= self.end:
                current_num = self.start
                self.start += self.increment
                return current_num
        else:
            if self.start <= self.end:
                current_num = self.start
                self.start += self.increment
                return current_num

        raise StopIteration


one_to_ten = custom_range(1,10,3)
for num in one_to_ten:
    print(num)
