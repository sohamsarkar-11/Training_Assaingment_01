def min_operations_to_equal(A, K):
    
    remainder = A[0] % K
    for num in A:
        if num % K != remainder:
            return -1

    base = remainder
    transformed = [(num - base) // K for num in A]
    transformed.sort()
    median = transformed[len(transformed) // 2]
    operations = sum(abs(x - median) for x in transformed)
    return operations

n = int(input())
A = list(map(int, input().split()))
K = int(input())

print(min_operations_to_equal(A, K))
