strings = ["hello", "world", "wassup", "oh!", "five", "score"]

def capitalize(strings):
    for word in strings:
        if len(word) < 5:
            yield word.capitalize()

print(set(capitalize(strings)))

