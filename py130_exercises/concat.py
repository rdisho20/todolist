from functools import reduce

strings = ["hello", "world", "wassup", " ", "oh!", "five"]

final = reduce(lambda x, y: x + y, strings)
print(final)