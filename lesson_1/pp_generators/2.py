def reciprocals(n):
    count = 1
    while count <= n:
        yield 1 / count
        count += 1

# generator = reciprocals(5)
for n in reciprocals(20):
    print(n)