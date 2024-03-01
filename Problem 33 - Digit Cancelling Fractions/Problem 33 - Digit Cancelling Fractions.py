from fractions import Fraction

def int_to_list(x):
    result = [int(digit) for digit in str(x)]
    return result

def list_to_int(x):
    y = []
    for digit in x:
        y.append(str(digit))
    result = "".join(y)
    result = int(result)
    return result

# print(list_to_int([9,2,3]))
def false_reduction(a,b):
    list_1 = int_to_list(a)
    list_2 = int_to_list(b)

    for x in list_1:
        if x in list_2:
            list_1.remove(x)
            list_2.remove(x)
            list_1 = list_to_int(list_1)
            list_2 = list_to_int(list_2)
            return [list_1, list_2]

    list_1 = list_to_int(list_1)
    list_2 = list_to_int(list_2)
    return [list_1, list_2]

print(false_reduction(30,31))

reduced_fractions = []

for a in range(10, 100):
    for b in range(a, 100):
        if false_reduction(a,b) != [a,b]:
            x = false_reduction(a,b)
            if x[0] < x[1] and x[0] != 0:
                reduced_fractions.append(false_reduction(a,b))

reduced_fractions_str = []
for frac in reduced_fractions:
    reduced_fractions_str.append(str(frac))

print(reduced_fractions)
print(set(reduced_fractions_str))
print(len(set(reduced_fractions_str)))
