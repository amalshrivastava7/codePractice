def solve(prefix, remainingString):

    if len(remainingString) == 0:
        print(prefix)
        return

    for i in range(len(remainingString)):
        prefix2 = prefix + remainingString[i]
        remainingString2 = remainingString
        remainingString2 = remainingString2.replace(remainingString[i], "")
        solve(prefix2, remainingString2)

solve("", "abcd")