lookup_table = {1:1, 89:89}


def square_digit_sum(x):
    square_digits = [int(i) * int(i) for i in list(str(x))]
    result = sum(square_digits)
    if result == 1:
        lookup_table[x] = 1
        return 1
    if result == 89:
        lookup_table[x] = 89
        return 89
    elif result in lookup_table:
        y = lookup_table[result]
        lookup_table[x] = y
        return y
    else:
        y = square_digit_sum(result)
        lookup_table[x] = y
        return y


n = 1
while n < 10_000_000:
    if n not in lookup_table:
        square_digit_sum(n)
        print(n)
    n += 1

final_list = [i for i in lookup_table if lookup_table[i] == 89]
print(len(final_list))
