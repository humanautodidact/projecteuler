def primes_less_than(n: int) -> list[int]:
    # set of primes less than 0,1, or 2 is {}
    if n <= 2:
        return []
    # array of n 1's
    is_prime = [1] * n
    # 0 and 1 are composite
    is_prime[0] = 0
    is_prime[1] = 0
    # having defined 0 and 1 as composite, we do 2<=i<n
    for i in range(2, n):
        # check if i is prime
        if is_prime[i] == 1:
            # if so, define all multiples of i as composite
            for j in range(2*i, n, i):
                is_prime[j] = 0
    # if n>2, return set of all primes less than 2
    return [i for i in range(n) if is_prime[i] == 1]


print(primes_less_than(10))
