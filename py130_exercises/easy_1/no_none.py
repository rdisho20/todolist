strings = ["hello", "world", None, "wassup", " ", "oh!", "five", None]

updated = filter(lambda string: string is not None, strings)

print(list(updated))