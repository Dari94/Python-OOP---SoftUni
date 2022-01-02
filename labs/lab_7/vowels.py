class vowels:
    def __init__(self,string):
        self.string = string
        self.vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.string):
            temp_index = self.current_index
            self.current_index +=1
            if self.string[temp_index].lower() in self.vowels_list:
                return self.string[temp_index]
            else:
                return self.__next__()
        raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
