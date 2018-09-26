import re
def word_count(filename):
    text = open(filename, "r")
    word_counts = {}
    for line in text:
        line = line.rstrip()
        line = line.split(" ")

        for word in line:
            word = re.sub(r'[^\w\s]','',word)
            word = word.lower()
            if word == "i":
                word = word.upper()
            word_counts[word] = word_counts.get(word, 0) + 1

    for key, val in word_counts.items():
        print key, val

    return word_counts


word_count("test.txt")

def sort_words(word_counts):
    word_counts = sorted(word_counts)
    print word_counts


word_counts = word_count("test.txt")
sort_words(word_counts)
