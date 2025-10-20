from stats import get_number_of_words, get_usage_by_character, get_sorted_list
import sys

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    usage_by_character = get_usage_by_character(book_text)
    sorted_list = get_sorted_list(usage_by_character)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

    

main()