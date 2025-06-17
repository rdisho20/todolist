adders = []
for n in range(1, 4):
    def add(x, n=n):
        return x + n

    adders.append(add)

print(n)

add1, add2, add3 = adders

print(add1(10))
print(add2(10))
print(add3(10))
print()
print(add1.__closure__)
print(add2.__closure__)
print(add3.__closure__)