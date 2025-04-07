    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    return len(book_text.split().lower())

def list_characters(book_text):
    return list(book_text)

def make_dict_from_list(new_list):
    dict_of_characters = {}
    for c in new_list:
        c = c.lower()
        if c in dict_of_characters:
            dict_of_characters[c] +=  1 
        else: dict_of_characters[c] = 1
    return dict_of_characters
   
