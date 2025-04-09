def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    Args:
    word (str): The word to check
    
    Returns:
    bool: True if the word is a palindrome, False otherwise
    """
    return word == word[::-1]


def find_palindromes(words):
    """
    Find palindromes in a list of words.
    
    Args:
    words (list): List of words to check
    
    Returns:
    list: List of palindromes found in the input list
    """
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes


# Test the functions
if __name__ == "__main__":
    word_list = ["radar", "hello", "level", "python", "madam"]
    palindromes = find_palindromes(word_list)
    print("Palindromes found:", palindromes)