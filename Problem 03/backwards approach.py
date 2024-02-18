from math import isqrt

x = int(input("Give me a number: "))

"""print(isqrt(x))
print(range(1, isqrt(x)))"""

"""range(isqrt(x), 1, -1)"""

"""
n = isqrt(x)
while x % n != 0 and [p for p in range(2, isqrt(n)) if n % p == 0] == []:
    n -= 1
else:
    print(n)
"""

n = isqrt(x)
while n > 1:

    x % n == 0 and [d for d in range(3, isqrt(n), 2) if n % d == 0] == []
    print("not found")
    n -= 1

# Test numbers: 13195, 600851475143
