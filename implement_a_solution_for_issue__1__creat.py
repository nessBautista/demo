def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    Parameters:
    word (str): The word to check if it is a palindrome.
    
    Returns:
    bool: True if the word is a palindrome, False otherwise.
    """
    return word.lower() == word[::-1].lower()


def find_palindromes(words):
    """
    Find palindromes in a list of words.
    
    Parameters:
    words (list): A list of words to check for palindromes.
    
    Returns:
    list: A list of palindromes found in the input list of words.
    """
    palindromes = [word for word in words if is_palindrome(word)]
    return palindromes


# Example usage
words_to_test = ['radar', 'python', 'level', 'stats', 'deified']
palindromes_found = find_palindromes(words_to_test)
print("Palindromes found in the list:", palindromes_found)