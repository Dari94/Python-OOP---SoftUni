from itertools import permutations


def possible_permutations(n_list):
    for per in permutations(n_list):
        yield list(per)
    #yield [per for per in permutations(n_list)]


[print(n) for n in possible_permutations([1, 2, 3])]
