def main():
    path = "./books/frankenstein.txt"
    print(get_book_text(path))

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

main()
