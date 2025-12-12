#!/usr/bin/env python3
# Statistical functions for analyzing text.
from collections import Counter
from typing import Any
import string


def get_num_words(text: str) -> int:
    """Return the total number of words in a text string.

    Args:
        text (str): The text to be processed.

    Returns:
        int: The total number of whitespace-separated words in the text.
    """
    return len(text.split())


def get_num_characters(text: str) -> dict[str, int]:
    """Count how many times each character appears in the text.

    The text is converted to lowercase before counting.

    Args:
        text (str): Text from a book or similar source.

    Returns:
        dict[str, int]: A mapping from each character to the number of times
            it appears in the text (including symbols and spaces).
    """
    text = text.lower()
    character_counts = dict(Counter(text))
    return character_counts


def sort_character_counts(character_counts: dict[str, int]) -> list[dict]:
    """Return a list of character counts sorted from most to least frequent.

    Args:
        character_counts (dict[str, int]): A mapping of characters to their counts.

    Returns:
        list[dict]: A list of dictionaries with the keys:
            - "char": the character
            - "num": the number of times it appears
            sorted in descending order by "num".
    """
    counts_list = []
    for char, num in character_counts.items():
        counts_list.append({"char": char, "num": num})
    counts_list.sort(reverse=True, key=sort_on)
    return counts_list


def sort_on(items):
    return items["num"]