import sys

from stats import get_num_of_words, sort_dictionaries, times_appeared


def get_book_text(file_path):
    file_contents = ""
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    word_count = get_num_of_words(file_contents)
    character_dict = times_appeared(file_contents)
    sorted_dictionaries = sort_dictionaries(character_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sorted_dictionary in sorted_dictionaries:
        if sorted_dictionary["char"].isalpha():
            print(f"{sorted_dictionary['char']}: {sorted_dictionary['num']}")
    print("============= END ===============")


main()
