import sys
from stats import get_num_words, get_char_count, get_sorted_char_count


def get_book_test(filepath: str):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_filepath = sys.argv[1]

    book_content = get_book_test(book_filepath)
    word_count = get_num_words(book_content)
    char_count = get_char_count(book_content)
    sorted_list_char_count = get_sorted_char_count(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for c_count in sorted_list_char_count:
        print(f"{c_count['char']}: {c_count['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
