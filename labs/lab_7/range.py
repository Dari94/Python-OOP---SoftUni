def genrange(start, end):
    num = start
    while num <= end:
        yield num
        num += 1


def genrange_1(start, end):
    for el in range(start, end + 1):
        yield el


print(list(genrange(2, 10)))
print(list(genrange_1(2, 10)))
