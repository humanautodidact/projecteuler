# 600851475143
x = int(input("Give me a number: "))
D = []

d = 2
while d <= x:
    if x % d == 0:
        D.append(d)
        print(d)
    d += 1

print(D)