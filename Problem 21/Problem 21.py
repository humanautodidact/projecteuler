def proper_factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1
    if x in result:
        result.remove(x)
    result.sort()
    return result

def d(n):
    return sum(proper_factors(n))

def amicable(a,b):
    if a != b and d(a) == b and d(b) == a:
        return True

amicable_numbers = []

n = int(input("Give me an integer: "))

for a in range(1,n):
    b = d(a)
    if amicable(a,b):
        if a not in amicable_numbers:
            amicable_numbers.append(a)
        if b not in amicable_numbers:
            amicable_numbers.append(b)


print(amicable_numbers)
print(sum(amicable_numbers))