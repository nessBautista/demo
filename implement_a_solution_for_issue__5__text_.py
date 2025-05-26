import re
from collections import Counter

def analyze_text(text):
    """
    Analyze the input text and return statistics.

    Args:
    text (str): Input text to analyze.

    Returns:
    dict: A dictionary containing the following statistics:
        - word_count
        - char_count
        - avg_word_length
        - most_common_word
        - sentence_count
        - paragraph_count
    """
    # Word count
    words = re.findall(r'\b\w+\b', text.lower())  # Case-insensitive word extraction
    word_count = len(words)

    # Character count (excluding spaces)
    char_count = sum(len(word) for word in words)

    # Average word length
    avg_word_length = char_count / word_count if word_count > 0 else 0

    # Most common word
    most_common_word = Counter(words).most_common(1)[0][0] if words else None

    # Number of sentences (assuming sentences end with '.', '!', or '?')
    sentence_count = len(re.findall(r'[.!?]', text))

    # Number of paragraphs (separated by double newlines)
    paragraph_count = len(re.findall(r'\n\s*\n', text)) + 1

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