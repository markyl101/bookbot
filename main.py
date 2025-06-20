from stats import get_word_count, stats, dict_sort
import sys

def get_book_text(book_path):
    file_contents = book_path.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = get_book_text(f)
        num_words = get_word_count(file_contents)
        freq = stats(file_contents)
        sorted_freq = dict_sort(freq)
    print("============ BOOKBOT =============")
    print(f"Analyzing {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_freq:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

initiate = main()