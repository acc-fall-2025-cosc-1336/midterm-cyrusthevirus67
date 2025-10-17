def get_sum_of_evens(num):
    """
    Returns the sum of all even numbers from 1 to num.
    Example: num = 10 -> 2 + 4 + 6 + 8 + 10 = 30
    """
    if num < 2:
        return 0
    return sum(range(2, num + 1, 2))
