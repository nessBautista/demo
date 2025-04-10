def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to a specified limit.

    Args:
    n (int): The upper limit for the Fibonacci sequence

    Returns:
    list: List of Fibonacci numbers less than or equal to the specified limit

    Raises:
    ValueError: If n is not a positive integer

    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a positive integer")

    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] + fibonacci_nums[-2] <= n:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])

    return fibonacci_nums

# Example usage
limit = 100
fibonacci_numbers = fibonacci_sequence(limit)
print(fibonacci_numbers)