def tags(par):
    def decorator(function):
        def wrapped(*args):
            result = function(*args)
            return f'<{par}>{result}</{par}>'
        return wrapped
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
