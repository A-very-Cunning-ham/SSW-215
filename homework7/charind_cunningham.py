def char_index(string, char):
    """returns a list of index values of each
    occurrence of the character `char` the string `string`"""
    matches = []
    for index, element in enumerate(string):
        if element == char:
            matches.append(index)

    print(f"The index values of each occurrences of character {char} in the string are {matches}")
    return matches

with open("homework7/fruits.txt", "r") as temp:
    fruits = temp.read().strip('"')

char_index(fruits, 'r')
