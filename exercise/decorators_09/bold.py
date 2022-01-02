def make_bold(function):
    def wrapped(*args):
        result = function(*args)
        return f'<b>{result}</b>'

    return wrapped


def make_italic(function):
    def wrapped(*args):
        result = function(*args)
        return f'<i>{result}</i>'

    return wrapped


def make_underline(function):
    def wrapped(*args):
        result = function(*args)
        return f'<u>{result}</u>'

    return wrapped


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
