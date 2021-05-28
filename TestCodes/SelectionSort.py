def SelectionSort(A):
    for i in range(len(A)-1):
        min_val = A[i]
        index = i
        j = i+1
        while(j<len(A)):
            if A[j] < min_val:
                min_val = A[j]
                index = j
            j = j+1
        # print(j)
        temp = A[i]
        A[i] = min_val
        A[index] = temp
        # print(A)
        # print(A)
    return(A)



print(SelectionSort([5,4,3,12, 33, 45, 76, 88, 99, 43, 25, 65]))
