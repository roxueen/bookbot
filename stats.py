def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(entry):
    return entry["num"]
    
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered.isalpha() or lowered in ",.?!:;'\"-":
                    if lowered in chars:
                        chars[lowered] +=1
                    else:
                        chars[lowered] = 1
    char_list = [{"char": c, "num": count} for c, count in chars.items()]
    char_list.sort(reverse=True, key = sort_on)
    return char_list

