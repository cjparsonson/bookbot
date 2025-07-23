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

def sort_on(items):
    return items['count']

def sort_dictionary(dictionary):
    list_of_dicts = [{"char": key, "count": value} for key, value in dictionary.items()]
    list_of_dicts.sort(key=sort_on, reverse=True)
    return list_of_dicts
