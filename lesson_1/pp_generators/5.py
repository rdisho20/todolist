strings = ["hello", "world", "wassup", "oh!", "five", "score"]
capitalize = (word.capitalize() for word in strings
              if len(word) >= 5)

print(set(capitalize))

