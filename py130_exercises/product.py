from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

product = reduce(lambda n, y: n * y, numbers)
print(product)