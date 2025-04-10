import re
from collections import Counter

def analyze_text(text):
    """
    Analyze the given text and return various statistics.

    Parameters:
    text (str): The input text to be analyzed.

    Returns:
    dict: A dictionary containing the following statistics:
        - word_count: Total number of words in the text
        - char_count: Total number of characters excluding spaces
        - avg_word_length: Average length of words in the text
        - most_common_word: Most common word in the text
        - sentence_count: Total number of sentences in the text
        - paragraph_count: Total number of paragraphs in the text
    """
    # Count words, characters, sentences, and paragraphs
    words = re.findall(r'\b\w+\b', text.lower())
    char_count = sum(len(word) for word in words)
    word_count = len(words)
    avg_word_length = char_count / word_count if word_count > 0 else 0
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    paragraph_count = len(re.findall(r'\n\s*\n', text))

    # Find the most common word
    word_freq = Counter(words)
    most_common_word = word_freq.most_common(1)[0][0] if word_freq else None

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