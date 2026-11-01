F = [1, 2]

n = 1
while F[n] + F[n-1] <= 4000000:
    f = F[n] + F[n - 1]
    print(f)
    F.append(f)
    n += 1

print(F)

E = [f for f in F if f % 2 == 0]

print(E)
print("The sum of even Fibs < 4 million is " + str(sum(E)))
