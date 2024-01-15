def students_study(time: int, coffee_needed: bool) -> bool:
    """Return True if students study in given circumstances."""
    if time >= 18 and time <= 24:
        return True
    elif time >= 5 and time <= 17 and coffee_needed == True:
        return True
    elif time >= 1 and time <= 4:
        return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """Return Lottery victory result 10, 5, 1, or 0 according to input values."""
    if a == b == c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and b != c and a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """Return number of small fruit baskets if it's possible to finish the order, otherwise return -1."""
    small_basket_capacity = 1
    big_basket_capacity = 5

    total_fruits = (big_baskets * big_basket_capacity) + (small_baskets * small_basket_capacity)

    if total_fruits < ordered_amount:
        return -1

    remaining_amount = ordered_amount
    small_baskets_needed = 0

    # Use big baskets first
    while big_baskets > 0 and remaining_amount >= big_basket_capacity:
        remaining_amount -= big_basket_capacity
        big_baskets -= 1

    # Use small baskets to fulfill the remaining amount
    small_baskets_needed = remaining_amount // small_basket_capacity

    return small_baskets_needed if remaining_amount % small_basket_capacity == 0 else -1
