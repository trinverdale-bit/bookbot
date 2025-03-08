import sys
from stats import count_words, count_characters

def get_book_text(filepath):
    try:
        with open(filepath) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: file {filepath} not found")
        sys.exit(1)

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]

    text = get_book_text(book)
    words = count_words(text)
    characters = count_characters(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    sorted_characters = sorted(characters.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_characters:
        print(f"{char}: {count}")

    print("============= END ===============")

main()
