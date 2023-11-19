"""Count words in file."""

def count_words(filename):
    word_count_dict = {}
    
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count_dict[word] = word_count_dict.get(word, 0) + 1

    return word_count_dict
