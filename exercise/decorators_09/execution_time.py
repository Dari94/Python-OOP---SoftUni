from timeit import default_timer as timer


# import time


def exec_time(function):
    def wrapped(*args):
        # start = time.time()
        start = timer()
        function(*args)
        # end = time.time()
        end = timer()
        return end - start

    return wrapped


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))
