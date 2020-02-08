queens = raw_input().split()

def checkResult(queens):
    N = len(queens)
    for r, c in enumerate(queens):
        row = int(r)
        col = int(c)
        for ir in range(row + 1, N):
            ic = int(queens[ir])
            if col == ic or abs(row - ir) == abs(col - ic):
                return False
    return True

print checkResult(queens)
