#!/usr/bin/env python3
# Statistical functions for ananlyzing text. 
from collections import Counter
import string

def get_num_words(text: str) -> int:
    """Count the total number of words in a text string.

    Args:
        text (str): The text to be processed

    Returns:
        int: The total number of words in the text
    """

    return len(text.split())

def get_num_characters(text: str) -> dict[str,int]:
    """
    Take the text from a book as a string and return the number of times each character appearewd in the text.

    Args:
        text (str): Text from a book or similar source.

    Returns:
        dict[str,int]: The number of times each character, including symbols and spaces appers in the text string.
    """
    text = text.lower()
    character_counts = dict(Counter(text))
    
    return character_counts