def add_item(characters, character, item):
    """Add the new item and initialize it with a quantity of 1"""
    characters[character].update({item: 1})
    return characters

def delete_item(characters, character, item):
    """Entirely remove the item from the character's inventory"""
    characters[character].pop(item)
    return characters

def increment_item(characters, character, item):
    """Increase the quantity of the item in the character's inventory by 1"""
    characters[character][item] += 1
    return characters

def decrement_item(characters, character, item):
    """Decrease the quantity of the item in the character's inventory by 1"""
    characters[character][item] -= 1
    if characters[character][item] == 0:
        print(f"The item {item} is now at zero in {character}'s inventory")
    return characters

def add_character(characters, character):
    """Add the character dict to the dict containing all characters"""
    characters.update(character)
    return characters


characters = {
    "Gandolf": {"food": 5, "grapefruit": 10, "green potions": 7, "red potions": 8, "spells of enchantment": 10},
    "Frodo": {"food": 0, "kiwi": 5, "wands of confusion": 7, "green potions": 8},
    "Sauron": {"bat wings": 5, "evil spells": 10, "fire wands": 5}
}

bilbo = {"Bilbo": {"food": 0, "kiwi": 5, "wands of confusion": 7, "green potions": 8}}

print("add item:")
print(add_item(characters, "Gandolf", "arandomitem"))

print("delete item:")
print(delete_item(characters, "Gandolf", "arandomitem"))

print("increment item:")
print(increment_item(characters, "Gandolf", "food"))

print("decrement item:")
print(decrement_item(characters, "Gandolf", "food"))

print("decrement to zero:")
print(increment_item(characters, "Frodo", "food"))
print(decrement_item(characters, "Frodo", "food"))

print("add character:")
print(add_character(characters, bilbo))