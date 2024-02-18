from math import isqrt


def prime_checker(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


n = int(input("Give me a number: "))

if prime_checker(n) == "prime":
    print("You gave me a prime number")

else:
    PF = []
    x = isqrt(n)
    print("The square root of " + str(n) + " rounded down is " + str(isqrt(n)))
    for x in range(isqrt(n), 1, -1):
        if n % x == 0 and prime_checker(x) == "prime":
            PF.append(x)

    print("The set of prime factors of " + str(n) + " is " + str(PF))
    print("The largest prime factor of " + str(n) + " is " + str(max(PF)))
# 1000003
# Test numbers: 13195, 600851475143
