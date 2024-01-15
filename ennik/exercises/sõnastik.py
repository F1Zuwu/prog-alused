def get_sum_and_diff(a: int, b: int) -> tuple:
    """
    Return sum of a and b and diff of a and b.
    """
    return a + b, a - b


def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    """
    Create a tuple.
    """
    return (a,) if a == b else (a, b)


def create_tuple_up_to_n(n: int) -> tuple:
    """
    Create tuple with numbers from 0 up to n (inclusive).
    """
    return tuple(range(n + 1)) if n >= 0 else ()


def merge_tuples(a: tuple, b: tuple) -> tuple:
    """
    Merge two tuples by adding b elements after a elements.
    """
    return a + b


def remove_odd_numbers(numbers: tuple) -> tuple:
    """
    Return a tuple where all the odd numbers are removed from the input tuple.
    """
    return tuple(x for x in numbers if x % 2 == 0)


def insert_tuple_inside_tuple(outer_tuple: tuple, position: int, inner_tuple: tuple) -> tuple:
    """
    Insert inner_tuple inside outer_tuple at the given position.
    """
    return outer_tuple[:position] + inner_tuple + outer_tuple[position:]
