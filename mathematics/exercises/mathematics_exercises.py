"""Math exercises."""
import math

def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    # Write your code here
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    division = round(num_a / num_b)
    return division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a + num_b) / 2.0
    return average



def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * radius**2
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> float:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = (math.sqrt(3) / 4) * side_length**2
    return triangle_area


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    discriminant = b**2 - 4*a*c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    c = math.sqrt(a**2 + b**2)
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of a cathetus when the lengths of the other cathetus and hypotenuse are given."""
    b = math.sqrt(c**2 - a**2)
    return b
