def words_count (text):
    return len(text.split())

def char_count (text):
    lower_text = text.lower()
    char_dic = {}
    for character in lower_text:
        if (character in char_dic):
            char_dic[character]=char_dic[character]+1
        else:
            char_dic[character] = 1
    return char_dic

def sort_on(items):
    return items["num"]


def sort_character(dictionary):
    char_num = []
    for key in dictionary:
        char_num.append({"letra": key, "num": dictionary[key]})
    
    char_num.sort(reverse=True, key=sort_on)
    return char_num
