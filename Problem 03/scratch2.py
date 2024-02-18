import math


x = int(input("Give me a number: "))
P = []

for n in range(1, math.sqrt(x)):
    if not [i for i in range(2, math.sqrt(n)) if n % i == 0]:
        P.append(p)
        print(p)
print(P)

