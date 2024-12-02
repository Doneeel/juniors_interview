def strict(func):
    def wrapper(*args, **kwargs):
        input_list = list(
            filter(lambda x: x[0] != "return", func.__annotations__.items())
        )

        arg_types = [type(i) for i in args]
        kwarg_types = [type(val) for val in kwargs.values()]

        parameter_types_got = arg_types + kwarg_types
        parameter_types_expected = [item[1] for item in input_list]

        if parameter_types_expected != parameter_types_got:
            raise TypeError("Got wrong parameter type")

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def bool_two(a: bool, b: bool) -> bool:
    return a == b


@strict
def sum_two_floats(a: float, b: float) -> float:
    return round(a + b, 1)


@strict
def sum_two_strs(a: str, b: str) -> str:
    return a + b
