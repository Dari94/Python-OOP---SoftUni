def cache(func):

    def wrapped(num):

        result = func(num)
        wrapped.log[num] = result
        return result
    wrapped.log = {}


    return wrapped


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)
