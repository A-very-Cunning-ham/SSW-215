def word_order(words):
    """Removes duplicate words and sorts the results"""
    wordList = sorted(set(words.split(", ")))
    result = ", ".join(wordList)
    print(result)
    return result


words = "apple, mango, carrot, apple, orange, mango, berry"

assert word_order(words) == "apple, berry, carrot, mango, orange"
