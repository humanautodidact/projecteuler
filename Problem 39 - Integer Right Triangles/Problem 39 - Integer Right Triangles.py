def num_of_solutions(p):
    n = 0
    for c in range(1, p+1):
        for b in range(1, c+1):
            a = p - b - c
            if a**2 + b**2 == c**2:
                n += 1
    return n


x = []
for p in range(0, 1001):
    x.append(num_of_solutions(p))
    print(p)

print("p = " + str(x.index(max(x))))
