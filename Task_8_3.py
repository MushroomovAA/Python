from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}: {arg} - {type(arg)}', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    """Number in cube"""
    return list(map(lambda x: x ** 3, args))


result = calc_cube(5, 8, 4, 7)

print(calc_cube.__name__)
print(calc_cube.__doc__)
print(type(calc_cube))
print(type(calc_cube()))
print(result)
