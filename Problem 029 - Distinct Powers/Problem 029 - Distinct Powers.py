combinations = []
for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in combinations:
            combinations.append(a**b)

combinations = sorted(combinations)
print(len(combinations))
