def recursiveSum(n):
    if n <= 1:
        return n
    else:
        return n + recursiveSum(n-1)

print(recursiveSum(16))