palindromes = []

for a in range(100, 1000):
    for b in range(100, 1000):
        if str(a*b) == str(a*b)[::-1]:
            palindromes.append(a*b)

print(max(palindromes))