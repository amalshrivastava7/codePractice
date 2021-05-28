## If all numbers in the array repeat except for one, find the element which does not repeat

def FindOddOneOut(A):
    xorsum = 0

    for item in A:
        xorsum = item^xorsum

    return(xorsum)


print(FindOddOneOut([2,3,4,5,9,8,8,9,4,3,2]))



