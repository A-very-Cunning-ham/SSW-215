def max_name_len(first, last):
    print(f"The largest value of the length of my firstname and lastname is {(largest := len(max(first, last)))}")
    return largest
    
max_name_len("avery", "cunningham")