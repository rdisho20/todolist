strings = ["hello", "world", "wassup"]

gen = (word.capitalize() for word in strings)
print(tuple(gen))