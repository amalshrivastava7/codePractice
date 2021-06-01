def TowerOfHanoi(n, S, T, D):

    if n == 1:
        print("move disc 1 from " + S + " to " + D)

        return -1

    TowerOfHanoi(n-1, S, D, T)

    print("move disc " + str(n) + " from " + S + " to " + D)

    TowerOfHanoi(n-1, T, S, D)



# print(TowerOfHanoi(, "one", "two", "three"))


def calcPower(a, n):

    if n == 1:
        return a

    return calcPower(a, n-1)*a

# print(calcPower(1, 3))

## TC : O(n)



def calcPower2(a, n):

    if n == 1:
        return a

    if n%2 == 0:
        k = calcPower2(a, n/2)
        return k*k
    else:
        k = calcPower2(a, n/2)
        return a*k*k

print(calcPower2(2, 4))


## TC: O(log n)


