import random

def make_hola_string(count: int) -> str:
    """
    Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    return "hola" * count

def generate_string_with_random_length(threshold: float) -> str:
    """
    Generate a string of "-" until a random number is below the threshold.

    Use random.random() to generate a random float.
    If the random number is below the threshold, add "-" to the result.
    If the random number is greater or equal to the threshold, finish the loop.

    generate_string_with_random_length(0.9) => "-----" (result can vary)
    generate_string_with_random_length(0.5) => "-" (usually empty or 1 minus)
    """
    result = ""
    while random.random() < threshold:
        result += "-"
    return result

def ask_user_age(age_limit: int) -> int:
    """
    Ask the user's age.

    You have to ask the user his/her age using input("What is your age?").
    You have to repeat this process until a correct age is entered.
    The age is correct if:
    - it is numeric (answering "a" is not correct)
    - it is greater or equal to the age_limit
    - it is less or equal to 100

    So, if the user enters a wrong age, the user gets a warning.
    The question is repeated until a correct age is entered.
    The function returns the correct age as an int.

    Warning is printed out:
    - non-numeric input: Wrong input!
    - age < age_limit: Too young!
    - age > 100: Too old!

    An example (with age_limit 18):
    What is your age? a
    Wrong input!
    What is your age? 10
    Too young!
    What is your age? 101
    Too old!
    What is your age? 21

    (function returns 21)
    """
    while True:
        age_str = input("What is your age? ")
        if not age_str.isnumeric():
            print("Wrong input!")
        else:
            age = int(age_str)
            if age < age_limit:
                print("Too young!")
            elif age > 100:
                print("Too old!")
            else:
                return age

# Example usage:
# age_limit = 18
# correct_age = ask_user_age(age_limit)
# print(f"You entered the correct age: {correct_age}")
