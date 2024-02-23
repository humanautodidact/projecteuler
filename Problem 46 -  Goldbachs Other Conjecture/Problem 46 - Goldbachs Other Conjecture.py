from math import isqrt
from math import ceil

def primality(m):
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"


# Iterate through each positive integer n with a while loop
found_counterexample = False
n = 1
while not found_counterexample:
    if n % 2 != 0 and primality(n) == "composite":
        # print(primes)
        # We need to build the prime list up to n-2. Since p <= n-2.
        conjecture = False
        for p in range(2, n):
            if primality(p) == "prime":
                for m in range(1, ceil(isqrt((n-2) // 2))+1):
                    if n == p + 2*m*m:
                        conjecture = True
                        print(str(n) + " = " + str(p) + " + 2" + "(" + str(m) + ")^2")
                        n += 1
        if not conjecture:
            found_counterexample = True
            print("Counterexample is n = " + str(n))
    n += 1




# If true, then move on to n+1

# If false for all those p and m, then print n and break the loop