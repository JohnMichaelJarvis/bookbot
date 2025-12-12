#!/usr/bin/env python3

from pathlib import Path
from stats import get_num_words


def main() -> None:
    book_path: str = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)

    print(f"Found {num_words} total words")


def get_book_text(filename: str | Path) -> str:
    """Read and output book text from a file.

    Args:
        filename (str | Path): the file to be read.

    Returns:
        str: A string containing all of the text in the book.
    """
    with open(filename, "r") as f:
        book_contents = f.read()

    return book_contents


if __name__ == "__main__":
    main()
