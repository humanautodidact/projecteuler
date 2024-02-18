fibonacci = [1,1]
fib_found = False

n = 2
while True:
    fibonacci.append(fibonacci[n-1]+fibonacci[n-2])
    if len(str(fibonacci[n])) >= 1000:
        print(n+1)
        break
    n += 1
