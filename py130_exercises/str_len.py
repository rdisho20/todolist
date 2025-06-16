strings = ["hello", "world", "wassup", "oh!", "five"]

new_list = map(lambda string: len(string), strings)
print(list(new_list))