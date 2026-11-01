n = 10
permutations = []

def f(A: list):
    # Base case:
    if len(A) == n:
        return
    else:
        for i in [k for k in range(0, n) if k not in A]:
            if len(A + [i]) == n:
                permutations.append(A + [i])
            f(A + [i])


f([])
permutations.sort()
millionth = permutations[999999]
millionthString = "".join(str(x) for x in millionth)
print(f"The millionth lexicographic permutation is {millionthString}.")
