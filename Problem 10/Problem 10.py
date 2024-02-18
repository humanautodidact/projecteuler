from math import isqrt


def primality(m):
    if m == 1:
        return "composite"
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


user_input = int(input("Give me a number: "))
primes = []

n = 1
while n < user_input:
    if primality(n) == "prime":
        print(n)
        primes.append(n)
    n += 1

print(sum(primes))
