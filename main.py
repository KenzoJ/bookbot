from stats import get_book_text, count_words

def main():
    path = "./books/frankenstein.txt"
    book_text = get_book_text(path)
    print(f'{count_words(book_text)} words found in the document')

main()
