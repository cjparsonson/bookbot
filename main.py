from stats import count_words, count_characters_occurrences

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_occurrences = count_characters_occurrences(book_text)
    print(f"{num_words} words found in the document")
    print(char_occurrences)

main()
