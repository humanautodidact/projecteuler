from math import isqrt

def primality(m):
    if m == 1:
        return "composite"
    if not [i for i in range(2, isqrt(m)+1) if m % i == 0]:
        return "prime"
    else:
        return "composite"

def rotation(x):
    string = str(x)
    y = [string[i] for i in range(1, len(string))] + [string[0]]
    result = str("".join(y))
    return result

def rotation_list(x):
    str_list = [str(x)]
    for i in range(0, len(str(x))):
        y = rotation(str_list[len(str_list)-1])
        if y in str_list:
            break
        else:
            str_list.append(y)
    result = []
    for i in str_list:
        result.append(int(i))
    return result

def is_circular(x):
    result = True
    for i in rotation_list(x):
        if primality(i) == "composite":
            result = False
            break
    return result

k = 0
n = 2
while n < 1_000_000:
    if is_circular(n):
        k += 1
    n += 1

print(k)
