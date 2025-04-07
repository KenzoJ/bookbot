from stats import get_book_text, count_words, list_characters, make_dict_from_list

def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    new_list = list_characters(book_text)
    dict_of_characters = make_dict_from_list(new_list)
    # print(f'{count_words(book_text)} words found in the document')
    print(dict_of_characters)

main()
