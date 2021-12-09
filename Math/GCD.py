def GCD(A, B):
    a = min(A, B)
    b = max(A, B)

    if a == 0:
        return b

    return(GCD(b%a, a))


print(GCD(12, 18))