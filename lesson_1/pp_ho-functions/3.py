def reduce(callback, iterable, current):
    for item in iterable:
        current = callback(item, current)
    
    return current


numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV


'''
1,0 = 1
2,1 = 3
4,3 = 7
8,7 = 15
16,15 = 31

'''