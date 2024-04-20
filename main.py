def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print()
    print(f"{num_words} found in the document.")
    print()
    print_char_dict(num_letters)
    print()
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_list_of_dict(dict):
    list_of_dict = []
    for key, value in dict.items():
        if key.isalpha():
            list_of_dict.append({"char": key, "num": value})
    return list_of_dict


def get_num_letters(text):
    letters = {}
    text = text.lower()
    for char in text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters


def get_num_words(text):
    words = text.split()
    return len(words)


def print_char_dict(dict):
    dict = get_list_of_dict(dict)
    dict.sort(reverse=True, key=sort_on)
    for item in dict:
        print(f"The '{item["char"]}' character was found {item["num"]} times.")


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()