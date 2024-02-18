def proper_factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x // i != i:
                result.append(x // i)
        i += 1
    if x in result:
        result.remove(x)
    result.sort()
    return result


# Consider the complement of the set of numbers which can be written as the
# sum of two abundant numbers. This is the set we wish to sum.
abundant_numbers = []
abundant_number_sums = []

# To compute numbers which can be written as the sum of two abundant
# numbers, we first have to calculate the proper factors of each number.
for n in range(1, 28124):
    # If the sum of the proper factors is > n, then add it to abundant numbers list.
    if sum(proper_factors(n)) > n:
        abundant_numbers.append(n)

# We now have a list of abundant numbers <= 28123
# Sum all pairs (x,y) where x and y are abundant numbers.
for x in abundant_numbers:
    for y in abundant_numbers:
        # Add each sum to abundant_numbers if the sum x+y is <= 28123
        if x + y <= 28123:
            abundant_number_sums.append(x + y)

# We now have found all abundant number sums <= 28123, including duplicates.
# We remove duplicates in the list.
abundant_number_sums = set(abundant_number_sums)
abundant_number_sums = list(abundant_number_sums)

# We now have found all unique abundant number sums.
# We make a list of all elements that are not abundant sums.
not_abundant_number_sums = [i for i in range(1, 28124) if i not in abundant_number_sums]

# Calculate the sum of this list.
print(sum(not_abundant_number_sums))
