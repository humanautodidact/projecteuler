# 600851475143
# First we create a program to find the prime factors of a number.
x = int(input("Give me a number: "))
P = [2]

p = 3
while p <= x / 2:
    if x % p == 0 and not [i for i in range(2, p) if p % i == 0]:
        P.append(p)
        print(p)
    p += 2


print("The prime factors of " + str(x) + " are " + str(P) + ".")
print("The largest prime factor is " + str(max(P)))
