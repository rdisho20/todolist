nested_numbers = [
    [1], [2], [3], [4], [5]
]

new_lst = list(num for lst in nested_numbers
               for num in lst)
print(new_lst)
