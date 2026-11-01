from math import isqrt


def is_prime(m):
    if m == 1:
        return False
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return True
    else:
        return False


results = []

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        if is_prime(abs(b)):
            n = 0
            while is_prime(abs(n**2 + a*n + b)):
                print((a, b))
                n += 1
            results.append((a*b, n))

results_second_coords = [i[1] for i in results]
maximum = max(results_second_coords)

for j in results:
    if j[1] == maximum:
        print("The maximum is " + str(j))
