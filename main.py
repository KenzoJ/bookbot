from stats import get_book_text, count_words, list_characters, make_dict_from_list, sort_dict, make_pretty_count

import sys 

def main():
    argu = sys.argv
    if len(argu) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(argu) == 2:
        print(argu[1])
        input_fix = f'./{argu[1].strip()}' 
        #path = "./books/frankenstein.txt"
        book_text = get_book_text(input_fix)
        new_list = list_characters(book_text)
        dict_of_characters = make_dict_from_list(new_list)
        # print(f'{count_words(book_text)} words found in the document')
        sorted_dict = sort_dict(dict_of_characters)
        print(f'============ BOOKBOT ============\nAnalyzing book found at {argu[1].strip()}...\n----------- Word Count ----------\nFound {count_words(book_text)} total words\n--------- Character Count -------')
        final_list = make_pretty_count(sorted_dict)
        for i in range(len(final_list)):
            print(final_list[i])
    else:
        print("Too many arguments")
        sys.exit(1)



main()
