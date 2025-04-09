def fibonacci_sequence(n):
    """
    Generate Fibonacci sequence up to a given number.

    Parameters:
    n (int): The upper limit for the Fibonacci sequence

    Returns:
    list: List of Fibonacci numbers less than or equal to n

    Raises:
    ValueError: If the input is not a positive integer

    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    fibonacci_list = [0, 1]
    next_fibonacci = 1

    while next_fibonacci <= n:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        if next_fibonacci <= n:
            fibonacci_list.append(next_fibonacci)

    return fibonacci_list

# Example usage
n = 100
print(fibonacci_sequence(n))