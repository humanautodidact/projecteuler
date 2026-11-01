from math import isqrt
from itertools import permutations

def is_prime(m):
    if m == 1:
        return False
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return True
    else:
        return False


def int_to_list(n):
    return [int(i) for i in str(n)]


def is_pandigital(x):
    length = len(str(x))
    if sorted(int_to_list(x)) == list(range(1, length + 1)):
        return True
    else:
        return False


pandigital_primes = []
all_perms = []
i = 1
while i <= 9:
    perms = permutations(list(range(1, i+1)))
    perms_as_ints = []
    for x in perms:
        y = int(''.join(map(str, x)))
        perms_as_ints.append(y)
    all_perms += perms_as_ints
    i += 1

all_perms.sort(reverse=True)

for perm in all_perms:
    print(perm)
    if is_prime(perm):
        break



#print(max(pandigital_primes))

#print(is_pandigital(987654321))
#print(is_prime(987654321))
