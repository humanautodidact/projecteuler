from fractions import Fraction
import math


minimum = Fraction(2,5)
maximum = Fraction(3,7)

for d in range(1, k + 1):
    # for numerator n < 8
    for n in range(1, int(math.ceil(k // 2))):
        if Fraction(n,d) < Fraction(2,5):
