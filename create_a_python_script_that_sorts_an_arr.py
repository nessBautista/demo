def sort_array_ascending(arr):
    """
    Sorts an array of numbers in ascending order.

    Args:
    arr (list): List of numbers to be sorted.

    Returns:
    list: Sorted list of numbers in ascending order.
    """
    sorted_arr = sorted(arr)
    return sorted_arr

# Test the function with an example array
if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 6, 3]
    sorted_numbers = sort_array_ascending(numbers)
    print(sorted_numbers)