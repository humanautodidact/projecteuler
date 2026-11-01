from fractions import Fraction
import math


result = []
# k = int(input("Give me an integer: "))
for k in [8,10,100,1000,10000]:
    # Create empty list for fractions
    fractions_list = []
    # for denominator d <= 8
    for d in range(1,k+1):
        # for numerator n < 8
        for n in range(int(math.floor(d // 2)), int(math.ceil(d // 2))):
            # append reduced fraction of n/d to fractions list
            fractions_list.append(Fraction(n, d))
            print(str(n)+"/"+str(d))
    # sort the list by size

    fractions_list.sort()
    fractions_list.append(Fraction(3, 7))

    i = fractions_list.index(Fraction(3, 7))
    # print(fractions_list[i-1])
    result.append(fractions_list[i-1])

print(result)
