def printSpiral(A):
    top = 0
    bottom = len(A)-1
    left = 0
    right = len(A[0])-1



    while (top<len(A) and bottom > -1 and left < len(A[0]) and right > -1):
        for i in range(left,right+1):
            print(A[top][i])
        top = top+1

        for i in range(top, bottom+1):
            print(A[i][right])
        right = right - 1

        for i in range(right,left-1,-1):
            print(A[bottom][i])
        bottom = bottom-1

        for i in range(bottom,top-1,-1):
            print(A[i][left])
        left = left+1



a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

print((printSpiral(a)))