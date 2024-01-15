def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.
    """
    if not s:
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.
    """
    sum_result = 0
    for i in range(n + 1):
        sum_result += i
    return sum_result


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.
    """
    pass


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.
    """
    if len(s) <= 1:
        return s
    elif s[0] == s[1]:
        return s[0] + '*' + pair_star_recursive(s[1:])
    else:
        return s[0] + pair_star_recursive(s[1:])
