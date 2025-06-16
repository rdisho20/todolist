def number_generator(num):
    for num in range(1, num + 1):
        yield num

for num in number_generator(5):
    print(num)