def word_count(text):
    return len(text.split())

def char_count(text):
    char_counter = {}
    for char in text:
        if char.lower() not in char_counter:
            char_counter[char.lower()] = 1
        else:
            char_counter[char.lower()] += 1
    return char_counter

def sort_char_dict(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({"char": char, "num": char_dict[char]})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list