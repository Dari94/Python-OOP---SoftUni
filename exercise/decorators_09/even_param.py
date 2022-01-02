def even_parameters(function):
    def wrapped(*args):

        for n in args:
            if isinstance(n, str):
                return "Please use only even numbers!"
        else:
            result = function(*args)
            new_list = [n for n in args if n % 2 == 0]

            if len(new_list) == len(args):
                return result
            return "Please use only even numbers!"

    return wrapped


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
