def is_permutation(a, b):
    string1 = list(str(a))
    string2 = list(str(b))
    digit_list1 = []
    digit_list2 = []

    for number in string1:
        digit_list1.append(int(number))

    for number in string2:
        digit_list2.append(int(number))

    digit_list1.sort()
    digit_list2.sort()

    if digit_list1 == digit_list2:
        return True
    else:
        return False


def is_permuted_multiple(x):
    for k in range(2, 7):
        if not is_permutation(x, k*x):
            return False
    return True


x = 2
while True:
    if is_permuted_multiple(x):
        print(x)
        break
    x += 1
