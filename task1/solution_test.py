from task1.solution import sum_two, bool_two, sum_two_floats, sum_two_strs


def sum_test() -> bool:
    assert sum_two(1, 2) == 3, "Wrong int"  # 3
    assert sum_two(1, b=2) == 3, "Wrong int"  # 3

    return True


def bool_test() -> bool:
    assert bool_two(True, False) is False, "Wrong boolean"  # False
    assert bool_two(a=False, b=False) is True, "Wrong boolean"  # True

    return True


def floats_test() -> bool:
    assert sum_two_floats(1.1, 2.2) == 3.3, "Wrong float"  # False
    assert sum_two_floats(a=1.1, b=2.2) == 3.3, "Wrong float"  # True

    return True


def strings_test() -> bool:
    assert sum_two_strs("Str1", "Str2") == "Str1Str2", "Wrong string"  # Str1Str2
    assert sum_two_strs(a="Str1", b="Str2") == "Str1Str2", "Wrong string"  # Str1Str2

    return True


def types_errors_test() -> tuple[type, bool]:
    try:
        sum_two(1, 2.4)
        return int, False
    except TypeError:
        pass

    try:
        bool_two(1, 2)
        return bool, False
    except TypeError:
        pass

    try:
        sum_two_floats(1, 2)
        return float, False
    except TypeError:
        pass

    try:
        sum_two_strs(1, 2)
        return str, False
    except TypeError:
        pass

    return None, True


def run():
    # [1] Type checking
    types_errors = types_errors_test()
    try:
        assert types_errors[1], True
    except AssertionError:
        print(f"TypeError was not raised for {types_errors[0]} type")

    print("[TASK1] [1 / 5] TypeError successfully raises for all functions")

    # [2] Sum int checking
    assert sum_test() is True, "Error in sum int function"

    print("[TASK1] [2 / 5] Sum for ints works properly")

    # [3] Bool func checking
    assert bool_test() is True, "Error in bool function"

    print("[TASK1] [3 / 5] Bool function works properly")

    # [4] Sum float checking
    assert floats_test() is True, "Error in sum floats function"

    print("[TASK1] [4 / 5] Sum for floats works properly")

    # [5] Sum strings checking
    assert strings_test() is True, "Error in string function"

    print("[TASK1] [5 / 5] Sum for strings works properly")
