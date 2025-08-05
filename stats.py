def sort_count(char_count):
    return char_count["num"]

def convert_to_list(char_count):
    num = []
    for count in char_count:
        new_dict = {"char": count, "num": char_count[count]}
        num.append(new_dict)
    num.sort(reverse = True, key = sort_count)
    return num

def get_char_counts(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_num_words(text):
    words = text.split()
    return len(words)