def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

def collatz_chain(n):
    chain = []
    i = 1
    while n != 1:
        chain.append(n)
        n = collatz(n)
        i += 1
    chain.append(1)
    return chain

chain_lengths = []
i = 1
while i < 1000000:
    chain_lengths.append(len(collatz_chain(i)))
    print(i)
    i += 1

max_start = chain_lengths.index(max(chain_lengths)) + 1
print(max_start)
print(max(chain_lengths))
#print(chain_lengths)
#print(collatz_chain(6))
#print(len(collatz_chain(6)))





#print(collatz(13))
#print(collatz_chain(13))
# print(collatz_chain(13))