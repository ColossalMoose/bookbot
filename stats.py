def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_usage_by_character(text):
    usage = {}
    for char in text:
        char = char.lower()
        usage[char] = usage.get(char, 0) + 1
    return usage

def sort_on(items):
    return items["num"]

def get_sorted_list(usage_dict):
    sorted_list = []
    for item in usage_dict:
        if item.isalpha():
            sorted_list.append({"char": item, "num": usage_dict[item]})
        #sorted_list.append((item, usage_dict[item]))
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
