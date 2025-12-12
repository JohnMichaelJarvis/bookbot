#! Python3
from pathlib import Path
from webbrowser import get


def main():
    book_text = get_book_text("books/frankenstein.txt")

    print(book_text)


def get_book_text(filename: str | Path) -> str:
    """
    Read and output book text from a file.

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
