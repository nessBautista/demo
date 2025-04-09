import re
from collections import Counter

def analyze_text(text):
    """Analyze the given text and return statistics.

    Args:
    text (str): The input text to be analyzed.

    Returns:
    dict: A dictionary containing the following statistics:
        - word_count: Total number of words in the text.
        - char_count: Total number of characters excluding spaces.
        - avg_word_length: Average word length in the text.
        - most_common_word: Most common word in the text.
        - sentence_count: Total number of sentences in the text.
        - paragraph_count: Total number of paragraphs in the text.
    """

    # Count words, characters, sentences, and paragraphs
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    avg_word_length = char_count / word_count if word_count > 0 else 0
    most_common_word = Counter(words).most_common(1)[0][0]

    sentences = re.split(r'[.!?]', text)
    sentence_count = len(sentences)

    paragraphs = re.split(r'\n\s*\n', text)
    paragraph_count = len(paragraphs)

    return {
        'word_count': word_count,
        'char_count': char_count,
        'avg_word_length': round(avg_word_length, 2),
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