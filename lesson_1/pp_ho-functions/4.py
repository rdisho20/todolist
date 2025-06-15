def reduce(callback, iterable, start):
    accum = start

    for item in iterable:
        accum = callback(item, accum)
    
    return accum

number_list = [3, 7, 2, 9, 5]
total = lambda number, accum: accum + number**2
print(reduce(total, number_list, 0))