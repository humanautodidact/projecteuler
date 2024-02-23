from math import isqrt
from itertools import permutations

def primality(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"

def int_to_list(n):
    return [int(i) for i in str(n)]

def is_triple_perm(x,y,z):
    if sorted(int_to_list(x)) == sorted(int_to_list(y)) == sorted(int_to_list(z)):
        return True
    else:
        return False

primes = [p for p in range(1_000, 10_000) if primality(p) == "prime"]

# We nest the for loops inside a function, and use 'return' when we want
# the program to stop. Otherwise, it is hard to exit all loops.
def f(x):
    for a in primes:
        for b in primes:
            for c in primes:
                if a < b < c:
                    if b-a == c-b:
                        if is_triple_perm(a,b,c):
                            print((a,b,c))
                            if (a, b, c) != (1487, 4817, 8147):
                                print(str(a)+str(b)+str(c))
                                return


# We use 1 as input, but it doesn't matter what we use as input
# because we just want the function to run and print the result.
print(f(1))
