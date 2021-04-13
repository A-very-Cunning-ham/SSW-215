def even_ind(str):
    """Removes characters at even indexes in `str`"""
    result = ""
    for i in range(len(str)):
        if i % 2 != 0:
            result += str[i]
    print(result)
    return result


even_ind("Individual software engineering")
