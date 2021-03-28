def char_index(string, char):
    """returns a list of index values of each
    occurrence of the character `char` the string `str`"""
    matches = []
    for index, element in enumerate(string):
        if element == char:
            matches.append(index)

    print(f"The index values of each occurrences of character {char} in the string are {matches}")
    return matches


fruits = "Mango banana apple pear Banana grapes strawberry Apple pear mango banana Kiwi apple mango strawberry"
char_index(fruits, "r")
