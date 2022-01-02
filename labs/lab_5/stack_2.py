class Stack(list):
    def push(self,value):
        self.append(value)
    def peek(self):
        return self[-1]
    def empty(self):
        return len(self) == 0