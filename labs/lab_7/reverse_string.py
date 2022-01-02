def reverse_text(string):
    num = len(string) - 1

    while num >= 0:
        yield string[num]
        num -= 1


def reverse_text_2(string):
    for letter in string[::-1]:
        yield letter


for char in reverse_text("step"):
    print(char, end='')
print('\n')
for char in reverse_text_2("step"):

    print(char, end='')

