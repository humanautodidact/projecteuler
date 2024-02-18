fibonacci = [1,1]
fib_found = False

n = 2
while not fib_found:
    fibonacci.append(fibonacci[n-1]+fibonacci[n-2])
    if len(str(fibonacci[n])) >= 1000:
        fib_found = True
        print(n+1)
    n += 1
