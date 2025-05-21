def count_words(text):
    words = text.split()
    return len(words)

def characters(text):
    char = {}
    new_text = text.lower()
    for i in new_text:
        if i in char:
            char[i] += 1
        else:
            char[i] = 1

    return char

def convert_to_list(char_dict):
    result = [{"char": key, "num": value} for key, value in char_dict.items()]
    def sort_on(dict_item):
        return dict_item["num"]

    result.sort(reverse=True, key=sort_on)
    

    return result