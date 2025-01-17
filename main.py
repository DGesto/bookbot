#print("hello world")
def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    #print(text)
    #print(count_words(text))
    #print(count_chars(text))
    
    total_words = count_words(text)
    char_count_dict = count_chars(text)
    
    print_report(file_path, total_words, char_count_dict)
    
    
def get_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def print_report(file_path, total_words, count_chars_dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{total_words} words found in the document")
    print()
    
    abc = list("abcdefghijklmnopqrstuvwxyz")
    for letter in abc:
        print(f"The '{letter}' character was found {count_chars_dict[letter]} times")
    print("--- End report ---")

main()