import math

def triangle(n):
    return sum(range(1,n+1))

def factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1
    return result


triangle_numbers = []

for i in range(1,11):
    triangle_numbers.append(triangle(i))

# Calculate triangle(n) until triangle(n) has over five hundred divisors. Until factors(triangle(n)) has length 501.

# Print triangle(n) once that happens

keep_going = True

i = 1
while keep_going:
    print(triangle(i))
    if len(factors(triangle(i))) > 500:
        print("found " + str(triangle(i)))
        keep_going = False
    i += 1

print(triangle_numbers)

print(factors(16))