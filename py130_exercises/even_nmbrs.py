numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def even(n):
    return n % 2 == 0

new_list = filter(even, numbers)
print(list(new_list))