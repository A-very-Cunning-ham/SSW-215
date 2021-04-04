def word_count(file):
    with open(file, "r") as temp:
        text = temp.read()

    words = text.split()
    word_count = len(words)

    print(f"The file {file} has about {word_count} words")
    return word_count


word_count("homework8/alice.txt")