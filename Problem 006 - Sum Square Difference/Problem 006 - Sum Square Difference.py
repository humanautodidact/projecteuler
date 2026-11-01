a = sum([n**2 for n in range(1, 101)])
print(a)

b = sum(list(range(1, 101))) ** 2
print(b)

print(b-a)