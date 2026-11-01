from math import isqrt


def primality(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


n = int(input("Give me a number: "))

if primality(n) == "prime":
    print("You gave me a prime number")

else:
    prime_factors = []
    x = isqrt(n)
    print("The square root of " + str(n) + " rounded down is " + str(isqrt(n)))
    for x in range(1, isqrt(n), 2):
        if n % x == 0 and primality(x) == "prime":
            prime_factors.append(x)

    print("The set of prime factors of " + str(n) + " is " + str(prime_factors))
    print("The largest prime factor of " + str(n) + " is " + str(max(prime_factors)))
# 1000003
# Test numbers: 13195, 600851475143
