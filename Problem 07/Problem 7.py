from math import isqrt


def primality(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


user_input = int(input("Give me a number: "))
primes = []

n = 1
while True:
    if primality(n) == "prime":
        primes.append(n)
    if len(primes) == user_input + 1:
        break
    n += 1

print(max(primes))
