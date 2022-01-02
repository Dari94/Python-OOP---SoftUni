def type_check(type_args):
    def decorator(function):
        def wrapped(*args):
            # if type(*args) == type_args:
            if isinstance(*args, type_args):
                result = function(*args)
                return result
            return 'Bad Type'

        return wrapped

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
