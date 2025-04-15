import sys
from stats import count_words, count_characters, sort_count_ascending

def get_book_text(filepath):
    book_contents = ""

    with open(filepath) as book:
        book_contents = book.read()

    return book_contents

def print_report(book_path, word_count, sorted_character_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_character_count:
        print(f"{entry}: {sorted_character_count[entry]}")
 

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    path_to_book = sys.argv[1] # "books/frankenstein.txt"
    
    book_text = get_book_text(path_to_book)

    num_words = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_count = sort_count_ascending(character_count)
    
    print_report(path_to_book, num_words, sorted_count)




main()