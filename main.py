import sys
from stats import count_words, count_characters_occurrences, sort_dictionary

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_occurrences = count_characters_occurrences(book_text)
    char_occurrences_sorted = sort_dictionary(char_occurrences)

    print("""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------""")
    for item in char_occurrences_sorted:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()
