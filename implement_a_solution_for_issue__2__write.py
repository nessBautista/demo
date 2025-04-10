def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to a given number.

    Args:
    n (int): Upper limit for Fibonacci numbers

    Returns:
    list: List of Fibonacci numbers less than or equal to n

    Raises:
    ValueError: If n is not a positive integer

    Example:
    >>> fibonacci_sequence(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci

# Example Usage
print(fibonacci_sequence(100))