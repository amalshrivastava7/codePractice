from codePractice.ArrayFunctions.ReverseArray import *

def transposeMatrix(A):
    for i in range(len(A)):
        j = i+1
        while j <len(A):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
            j = j+1
    return A


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print((transposeMatrix(a)))


## Rotate Matrix - Transpose + reverse every row

def rotateMatrix(A):
    A = transposeMatrix(A)

    # print(A)
    for i in range(len(A)):
        A[i] = reverseArray(A[i])

    return(A)

a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print((rotateMatrix(a)))