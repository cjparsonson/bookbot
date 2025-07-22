def count_words(text):
    words = text.split()
    return len(words)

def count_characters_occurrences(text):
    char_occurences_dict = {}
    for char in text:
        char = char.lower()
        if char in char_occurences_dict:
            char_occurences_dict[char] += 1
        else:
            char_occurences_dict[char] = 1
    return char_occurences_dict
