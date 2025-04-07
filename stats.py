
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    return len(book_text.split())
