from math import isqrt


def primality(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


print(primality(2))
print(primality(3))
print(primality(5))
print(primality(11))
print(primality(15))
