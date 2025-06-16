string = "Hello, world!"

reverse = (string[idx] for idx in range(len(string) - 1, -1, -1))
print(''.join(reverse))