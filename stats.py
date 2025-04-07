def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    return len(book_text.split())

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
  
def sort_on(dict):
    return dict["num"]

def sort_dict(ex_list):
    temp_list = []
    for k, v in ex_list.items():
        if k.isalpha():
            temp_d = {"name": k, "num": v}
            temp_list.append(temp_d)

    temp_list.sort(reverse=True, key=sort_on)
    return temp_list

def make_pretty_count(l):
    final_list = []
    for i in range(len(l)):
        formatted_string = f'{l[i]["name"]}: {l[i]["num"]}'
        final_list.append(formatted_string)
    return final_list


