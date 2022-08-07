import functools


class UnexpectedTypeException(ValueError):
    def __init__(self, output_num, func_name, expected_output_type):
        self.error = f'The {output_num} argument of {func_name}() is not a {expected_output_type}'

    def __str__(self):
        return self.error


def expected(*expected_output_types):
    def output_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            outputs = func(*args, **kwargs)

            for i, types in enumerate(zip(outputs, expected_output_types)):
                if not type(types[0]) is types[1]:
                    raise UnexpectedTypeException(i + 1, func.__name__, types[1])
            return outputs

        return wrapper

    return output_decorator


@expected(str)
def test_valid():
    return 'ttt'

@expected(str, int, int)
def test_invalid():
    return 'str', 5, 'str'


if __name__ == '__main__':
    test_invalid()