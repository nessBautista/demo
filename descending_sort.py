def sort_numbers_descending(numbers):
    """
    Sorts a list of numbers in descending order.
    
    Args:
        numbers (list): A list of numbers (integers or floating-point numbers)
    
    Returns:
        list: A new list containing the numbers sorted in descending order
    
    Raises:
        TypeError: If the input is not a list or contains non-numeric values
    
    Example:
        >>> sort_numbers_descending([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers")
    
    # Create a copy to avoid modifying the original list
    sorted_list = numbers.copy()
    
    # Sort in descending order
    sorted_list.sort(reverse=True)
    
    return sorted_list


# Example usage
if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = sort_numbers_descending(numbers)
    print("Original list:", numbers)
    print("Sorted list (descending):", sorted_numbers)
    
    # Verify the original list is unchanged
    print("Is original list unchanged?", numbers == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    
    # Test with floating point numbers
    float_numbers = [3.14, 1.618, 2.718, 0.577, 1.414]
    sorted_float_numbers = sort_numbers_descending(float_numbers)
    print("\nOriginal float list:", float_numbers)
    print("Sorted float list (descending):", sorted_float_numbers)