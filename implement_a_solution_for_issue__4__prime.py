def is_prime(n):
    """
    Check if a given number is prime.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """
    Find all prime numbers within a specified range.

    Args:
    start (int): The starting value of the range.
    end (int): The ending value of the range.

    Returns:
    list: A list of prime numbers within the specified range.
    """
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
start_range = 10
end_range = 50
prime_numbers = find_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {prime_numbers}")