def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}

    for char in text.lower():
        if char.isspace():
            continue
        elif char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters
