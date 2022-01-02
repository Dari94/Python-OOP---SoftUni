from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        vowels = ['a', 'e', 'o', 'i', 'u']
        return [x for x in result if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters)
print(get_letters())
