def create_set_from_numbers(a: int, b: int, c: int) -> set:
    return {a, b, c}


def add_one(set_a: set) -> set:
    return {x + 1 for x in set_a}


def remove_six(set_a: set) -> set:
    return set_a - {6}


def convert_to_set(list_a: list) -> set:
    return set(list_a)


def count_unique_elements(input_list: list) -> int:
    return len(set(input_list))


def common_characters_in_words(word1: str, word2: str) -> set:
    return set(word1) & set(word2)


def exam_conditions_not_met(names1: list, names2: list) -> set:
    return set(names1) ^ set(names2)


def uninvited_friends_count(friends: list, invited: list) -> int:
    return len(set(friends) - set(invited))


def contains_duplicates(input_list: list) -> bool:
    return len(input_list) != len(set(input_list))


def find_numbers_divisible_by_3(numbers: list) -> set:
    divisible_by_3 = set(range(0, 1001, 3))
    return set(numbers) & divisible_by_3
