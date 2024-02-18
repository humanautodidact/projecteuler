def f(n):
    # Base cases:
    if n == 1:
        return 1
    if n == 2:
        return 1
    # Recursive formula
    if n > 2:
        return f(n-1) + f(n-2)


i = 0
while True:


fib_found = False
n = 1
while not fib_found:
    print(f(n))
    if len(str(f(n))) >= 1000:
        fib_found = True
        print("n = " + str(n))
        print("f(n) = " + str(f(n)))
    n += 1
