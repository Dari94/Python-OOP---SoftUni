def read_next(*args):
    print(type(args))
    for seq in args:
        for el in seq:
            yield el


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
