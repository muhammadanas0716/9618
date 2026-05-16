def IterativeSum(N: int):
    total = 0

    for count in range(1, N + 1):
        total = total + count

    return total

print(IterativeSum(5))


def RecursiveSum(N: int):
    if N == 0:
        return 0

    return N + RecursiveSum(N - 1)


print(RecursiveSum(5))