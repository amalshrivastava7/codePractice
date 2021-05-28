def reverseArray(A):
    for i in range(0,len(A)/2):
        temp = A[i]
        A[i] = A[len(A)-1-i]
        A[len(A)-1-i] = temp

    return(A)


# print(reverseArray([1,2,3,4,5,6]))


## Reverse array by k steps


def reverseArrayKSteps(A, k):
    B = reverseArray(A)

    x = reverseArray(B[0:k])
    y = reverseArray(B[k:(len(B))])

    return(x+y)

# print(reverseArrayKSteps([1,2,3,4,5,6], 3))




