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
            word_counts[word] = word_counts.get(word, 0) + 1
    print word_counts
    return word_counts


word_count("test.txt")
