"""Exercises for if statement."""


def are_equal(num_a: int, num_b: int) -> str:
    """
    Return "equal" if given numbers are equal and "not equal" if not.

    are_equal(12, 13) => "not equal"
    are_equal(5, 5) => "equal"

    :param num_a: first number
    :param num_b: second number

    :return: "equal" if given numbers are equal and "not equal" if they aren't.
    """
    # your code goes here
    if num_a == num_b:
        return "equal"
    else:
        return "not equal"

# Test the function
print(are_equal(12, 13))
print(are_equal(5, 5))



def positive_or_negative(num_a: int) -> str:
    """
    Return "negative", "positive" or "zero" depending on the given integer.

    positive_or_negative(12) => "positive"
    positive_or_negative(0) => "zero"
    positive_or_negative(-12) => "negative"

    :param num_a: given integer
    :return "negative", "positive" or "zero" depending on the given integer.
    """
    # your code goes here
    if num_a > 0:
        return "positive"
    elif num_a < 0:
        return "negative"
    else:
        return "zero"

# Test the function
print(positive_or_negative(12))
print(positive_or_negative(0))
print(positive_or_negative(-12))


def is_in_string(letter: str, word: str) -> bool:
    """
    If the given letter is in the given word, return True, else return False.

    is_in_string("a", "car") => True
    is_in_string("b", "car") => False

    :param letter: given letter.
    :param word: given word.
    :return: boolean depending on if the given letter is in the given word.
    """
    return letter in word

# Test cases
print(is_in_string("a", "car"))
print(is_in_string("b", "car"))



def are_same_length(str_a: str, str_b: str) -> bool:
    """
    Return True if given strings are of equal length or False if not.

    are_same_length("aa", "bb") => True
    are_same_length("a", "bbb") => False

    :param str_a: first string
    :param str_b: second string
    :return: boolean True or False.
    """
    return len(str_a) == len(str_b)

# Test cases
print(are_same_length("aa", "bb"))
print(are_same_length("a", "bbb"))


def is_letter_or_digit(symbol: str) -> str:
    """
    Return "letter" if given symbol is a letter, "digit" if given symbol is a digit, and "other" if it's neither.

    is_letter_or_digit("a") => "letter"
    is_letter_or_digit("1") => "digit"
    is_letter_or_digit("?") => "other"

    :param symbol: symbol
    :return "letter", "digit", or "other".
    """
    if symbol.isalpha():
        return "letter"
    elif symbol.isdigit():
        return "digit"
    else:
        return "other"

# Test cases
print(is_letter_or_digit("a"))
print(is_letter_or_digit("1"))
print(is_letter_or_digit("?"))



def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    """
    Given two strings, return True if last symbols are the same and False if not.

    are_last_symbols_same("car", "house") => False
    are_last_symbols_same("bird", "card") => True

    :param str_a: first string.
    :param str_b: second string.
    :return boolean.
    """
    # your code goes here
    return str_a[-1] == str_b[-1]

# Test cases
print(are_last_symbols_same("car", "house"))
print(are_last_symbols_same("bird", "card"))



def hundred(num_a: int) -> int:
    """
    Given a positive integer num_a. If its smaller or equal to 100 return 100 - num_a. Else return the reminder from dividing it with 100.

    hundred(45) => 55
    hundred(100) => 0
    hundred(110) => 10

    :param num_a: given positive integer
    :return int.
    """
    # your code goes here
    if num_a <= 100:
        return 100 - num_a
    else:
        return num_a % 100

# Test cases
print(hundred(45))   # Output: 55
print(hundred(100))  # Output: 0
print(hundred(110))  # Output: 10
