def get_num_of_words(words):
    split_words = words.split()
    num_of_words = len(split_words)

    return num_of_words


def times_appeared(words):
    times_appeared_dict = {}
    for word in words.strip():
        word_lowercased = word.lower()
        if word_lowercased in times_appeared_dict:
            times_appeared_dict[word_lowercased] += 1
        else:
            times_appeared_dict[word_lowercased] = 1
    return times_appeared_dict


def sort_dictionaries(dictionary):
    list_of_dicts = []
    sorted_dictionaries = dict(
        sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    )
    for item in sorted_dictionaries:
        list_of_dicts.append({"char": item, "num": sorted_dictionaries[item]})
    return list_of_dicts
