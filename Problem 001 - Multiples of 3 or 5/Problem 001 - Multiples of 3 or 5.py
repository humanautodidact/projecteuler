# Multiples of 3 or 5
N = range(0,1000)

# Find the multiples of 3 or 5 in N
A = [x for x in N if x % 3 == 0 or x % 5 == 0]

# Print the sum of all the multiples.
print(sum(A))