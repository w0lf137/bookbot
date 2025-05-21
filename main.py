from stats import count_words
from stats import characters
from stats import convert_to_list
import sys


def get_book_text(filepath):
    with open(filepath) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents



def main():
    #book_text = get_book_text("books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    dictionary = characters(book_text)
    result = convert_to_list(dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # Loop through the sorted list
    for char_dict in result:
        char = char_dict["char"]
        count = char_dict["num"]
        # Only print alphabetic characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")



main()