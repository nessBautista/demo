def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to a given number.

    Parameters:
    n (int): The limit of the Fibonacci sequence

    Returns:
    list: Fibonacci numbers less than or equal to n

    Raises:
    ValueError: If n is not a positive integer

    Examples:
    >>> fibonacci_sequence(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    fibonacci_list = [0, 1]
    while True:
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        if next_fibonacci <= n:
            fibonacci_list.append(next_fibonacci)
        else:
            break

    return fibonacci_list


# Example usage
if __name__ == "__main__":
    result = fibonacci_sequence(100)
    print(result)