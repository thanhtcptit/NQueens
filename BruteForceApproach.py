import time
def is_queen_safe(queens, row, col):
    for r, c in enumerate(queens):
        if r == row or c == col or abs(row - r) == abs(col - c):
            return False
    return True

def print_the_board(queens, N):
    for row in range(N):
        print queens[row],

def solution(N):
    queens = []
    col = row = 0
    flag = True
    while flag:
        while col < N and not is_queen_safe(queens,row, col):
            col += 1
        if col < N:
            queens.append(col)
            if row + 1 == N:
                print_the_board(queens, N)
                queens.pop()
                col = N
                flag = False
                break
            else:
                row += 1
                col = 0
        if col >= N:
            if row == 0:
                return
            col = queens.pop() + 1
            row -= 1

start = time.time()
solution(22)
print "\n---- %f seconds ----" % (time.time() - start)