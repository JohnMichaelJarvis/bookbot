#!/usr/bin/env python3


def get_num_words(text: str) -> int:
    """Count the total number of words in a text string.

    Args:
        text (str): The text to be processed

    Returns:
        int: The total number of words in the text
    """

    return len(text.split())
