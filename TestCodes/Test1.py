def solve(A):
    B = sorted(A)

    diff = 0
    set = False

    print(B)

    for i in range(len(B)-1):
        newdiff = A[i+1] - A[i]
        print(newdiff)
        if set and newdiff != diff:
            return 0
        else:
            set = True
            diff = newdiff
    return 1

print(solve([3,5,1]))