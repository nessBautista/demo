import re
from collections import Counter

def analyze_text(text):
    """
    Analyze the input text and return statistics.

    Args:
        text (str): Input text to analyze.

    Returns:
        dict: Dictionary containing various statistics.
    """
    # Count words, characters, and sentences
    words = text.lower().split()
    char_count = len(text.replace(" ", ""))
    avg_word_length = sum(len(word) for word in words) / len(words)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    # Count paragraphs
    paragraphs = re.split(r'\n\s*\n', text)
    paragraph_count = len(paragraphs)
    
    # Find the most common word
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)[0][0]
    
    # Prepare the statistics dictionary
    stats = {
        'word_count': len(words),
        'char_count': char_count,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count
    }
    
    return stats

# Example usage
text = """This is a sample text. It contains multiple sentences.
And even multiple paragraphs.

This is the second paragraph. It helps demonstrate the analyzer."""

stats = analyze_text(text)
print(stats)