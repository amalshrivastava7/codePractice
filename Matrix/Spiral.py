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

def generateMatrix(self, A):
    n = A
    ret = [[0]*n]
    for i in range(n-1):
        ret.append([0]*n)

    T = 0
    B = n-1
    L = 0
    R = n-1
    direction = 0
    num = 1
    while T <= B and L <= R:
        if direction == 0:
            for i in range(L, R+1):
                ret[T][i] = num
                num += 1
            T += 1
            direction = 1
        elif direction == 1:
            for i in range(T, B+1):
                ret[i][R] = num
                num += 1
            R -= 1
            direction = 2
        elif direction == 2:
            for i in range(R, L - 1, -1):
                ret[B][i] = num
                num += 1
            B -= 1
            direction = 3
        else:
            for i in range(B, T - 1, -1):
                ret[i][L] = num
                num += 1
            L += 1
            direction = 0
    return ret