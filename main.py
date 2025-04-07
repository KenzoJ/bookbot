from stats import get_book_text, count_words, list_characters, make_dict_from_list, sort_dict, make_pretty_count

def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    new_list = list_characters(book_text)
    dict_of_characters = make_dict_from_list(new_list)
    # print(f'{count_words(book_text)} words found in the document')
    sorted_dict = sort_dict(dict_of_characters)
    print(f'============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound {count_words(book_text)} total words\n--------- Character Count -------')
    final_list = make_pretty_count(sorted_dict)
    for i in range(len(final_list)):
        print(final_list[i])

main()
