def get_chars_set(path):
    """
    Expect a text file that each line is a char
    """
    chars = list()
    with open(path, encoding='utf8') as f:
        for line in f:
            line = u"%s" % line
            char = line.split()[0]
            print(char)
            chars.append(char)
    return chars

if __name__ == "__main__":
    get_chars_set("charsets/top_3000_simplified.txt")