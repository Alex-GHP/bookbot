def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_freq = get_chars_freq(text)
    char_list = chars_dict_to_sorted_list(chars_freq)
    print_book_report(char_list, num_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = len(text.split())
    return words


def get_chars_freq(text):
    chars_dict = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_book_report(chars_list, num_words):
    print("=== REPORT of books/frankenstein.txt ===")
    print(f"{num_words} found in the book")
    print()
    
    for char in chars_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times.")
    print()

    print("=== END REPORT ===")


main()
