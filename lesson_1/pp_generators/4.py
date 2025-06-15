strings = ["hello", "world", "wassup"]

def capitalize(strings):
    count = 0
    while count < len(strings):
        yield strings[count].capitalize()
        count += 1

print(tuple(capitalize(strings)))

