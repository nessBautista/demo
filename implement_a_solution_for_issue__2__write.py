def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence up to a given number.

    Args:
    n (int): The limit up to which the Fibonacci sequence will be generated.

    Returns:
    list: List of Fibonacci numbers less than or equal to n.

    Raises:
    ValueError: If n is not a non-negative integer.

    Example:
    >>> fibonacci_sequence(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    fibonacci_list = [0, 1]
    while True:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        if next_fibonacci <= n:
            fibonacci_list.append(next_fibonacci)
        else:
            break

    return fibonacci_list

# Example usage
print(fibonacci_sequence(100))