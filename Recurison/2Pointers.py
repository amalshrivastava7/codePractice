def findSum(A, k):

    j = len(A) - 1

    for i in range(0, len(A)):

        if (A[i] + A[j] == k):
            print("reached")
            print(i)
            print(j)
            return True

        while A[i] + A[j] > k and j>i:
            print("i = ", i)
            print("j = ", j)
            j = j-1

    return False


print(findSum([5, 8, 13, 17, 31], 99))