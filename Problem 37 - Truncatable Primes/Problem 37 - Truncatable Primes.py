from math import isqrt


def is_prime(m):
    if m == 1:
        return False
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return True
    else:
        return False


def left_remove(x):
    y = list(str(x))
    y.remove(y[0])
    result = "".join(y)
    result = int(result)
    return result


def right_remove(x):
    y = list(str(x))
    y.pop()
    result = "".join(y)
    result = int(result)
    return result


def is_truncatable(x):
    if x in range(0,10):
        return False
    else:
        result = True
        y = x
        i = 0
        while len(str(y)) > 1:
            y = left_remove(y)
            if not is_prime(y):
                result = False
            i += 1

        z = x
        k = 0
        while len(str(z)) > 1:
            z = right_remove(z)
            if not is_prime(z):
                result = False
            k += 1

        return result


truncatable_primes = []

n = 0
while len(truncatable_primes) < 11:
    if is_truncatable(n) and is_prime(n):
        truncatable_primes.append(n)
        print(n)
    n += 1

truncatable_sum = sum(truncatable_primes)

print(truncatable_primes)
print("The sum is " + str(truncatable_sum))