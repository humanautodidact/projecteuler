from math import isqrt


# Sieve of Eratosthenes
n = int(input("Give me a number greater than 2: ")) + 1
# list of n 1's
is_prime = [1] * n
# 0 and 1 are composite
is_prime[0] = 0
is_prime[1] = 0
# having defined 0 and 1 as composite, we consider values from 2 to n-1
for i in range(2, isqrt(n)):
    # check if i is prime
    if is_prime[i] == 1:
        # if so, define all multiples of i as composite
        for j in range(i * i, n, 2 * i):
            is_prime[j] = 0
# If user gives number >2, then there are prime numbers, and we print the list of primes
# as found by the Sieve of Eratosthenes.
if n > 2:
    primes_less_than = [i for i in range(n) if is_prime[i] == 1]
    prime_factors = [i for i in primes_less_than if (n-1) % i == 0]
    print("The largest prime factor of " + str(n - 1) + " is " + str(max(prime_factors)) + ".")

# Test numbers: 13195, 600851475143
