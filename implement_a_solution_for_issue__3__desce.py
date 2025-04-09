def sort_numbers_descending(numbers):
    """
    Sort a list of numbers in descending order.

    Args:
    numbers (list of int or float): List of numbers to be sorted.

    Returns:
    list: A new list with the numbers sorted in descending order.

    Example:
    >>> numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    >>> sorted_numbers = sort_numbers_descending(numbers)
    >>> print(sorted_numbers)
    [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
    """
    # Create a new list with the sorted numbers in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers