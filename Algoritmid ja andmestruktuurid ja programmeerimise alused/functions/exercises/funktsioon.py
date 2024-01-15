"""Function examples."""

 
# func()
def func():
    print("I´m inside the function")

# my_name_is(name)
def my_name_is(string):
    print("My name is " + string)

# sum_six(num)`
def sum_six(int):
    return 6 + int


# sum_numbers()
def sum_numbers(a, b):
    return a + b
# usd_to_eur()

def usd_to_eur(int):
    exchange_rate = 0.8
    eur = int * exchange_rate
    return eur