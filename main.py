#!/usr/bin/env python3
from pathlib import Path
from stats import get_num_words, get_num_characters, sort_character_counts
import sys


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path: str = sys.argv[1]
    book_text: str = get_book_text(book_path)

    num_words: int = get_num_words(book_text)
    num_characters: dict[str,int] = get_num_characters(book_text)
    sorted_num_characters: list[dict] = sort_character_counts(num_characters)


    # formatted_counts: str = ""
    # for char_count in sorted_num_characters:
    #     for character_name,character_count in char_count.items():
    #        if character_name.isalpha(): 
    #         formatted_counts += f"{character_name}: {character_count}\n"


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(formatted_counts)
    for char_count in sorted_num_characters:
        ch = char_count["char"]
        count = char_count["num"]

        if not ch.isalpha():
            continue

        print(f"{ch}: {count}")         
    print("============= END ===============")


def get_book_text(filename: str | Path) -> str:
    """Read and return the book text from a file.

    Args:
        filename (str | Path): Path to the file to read.

    Returns:
        str: The text contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(filename, "r") as f:
        book_contents = f.read()

    return book_contents


if __name__ == "__main__":
    main()
