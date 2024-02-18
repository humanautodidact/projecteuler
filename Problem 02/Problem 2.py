# How to avoid IndexError if we do not yet know that the index of the
# last Fib under 4 million is 32? IndexError occurs once we get to the
# 33th Fib. To replicate error, replace 32 with 4000001

F = [1, 2]

for n in range(1, 4000001):
    if (F[n] + F[n-1]) <= 4000000:
        f = F[n] + F[n-1]
        F.append(f)
    else:
        break
print(F)

E = [f for f in F if f % 2 == 0 and f < 4000001]
print("The sum of even Fibs < 4 million is " + str(sum(E)))
