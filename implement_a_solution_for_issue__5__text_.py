import re
from collections import Counter

def analyze_text(text):
    """
    Analyzes the given text and provides various statistics.

    Args:
    text (str): The input text to analyze.

    Returns:
    dict: A dictionary containing the following statistics:
        - word_count: Total number of words in the text
        - char_count: Total number of characters excluding spaces
        - avg_word_length: Average length of words
        - most_common_word: Most common word in the text
        - sentence_count: Total number of sentences
        - paragraph_count: Total number of paragraphs
    """

    # Count words
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)

    # Count characters excluding spaces
    char_count = len(''.join(words))

    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0

    # Find the most common word
    word_counter = Counter(words)
    most_common_word = word_counter.most_common(1)[0][0] if word_counter else None

    # Count sentences
    sentence_count = text.count('.') + text.count('?') + text.count('!')

    # Count paragraphs
    paragraph_count = max(0, text.count('\n\n'))

    return {
        'word_count': word_count,
        'char_count': char_count,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count
    }

# Example usage
text = """This is a sample text. It contains multiple sentences.
And even multiple paragraphs.

This is the second paragraph. It helps demonstrate the analyzer."""
stats = analyze_text(text)
print(stats)