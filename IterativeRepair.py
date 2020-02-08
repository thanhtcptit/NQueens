import time
import random

N = 1000

def init():
    global last_iterative_queen, loop_count, left_diagonal, right_diagonal, cols, queens
    left_diagonal = [0 for i in range(0, 2 * N)]
    right_diagonal = [0 for i in range(0, 2 * N)]
    cols = [0 for i in range(0, N)]
    last_iterative_queen = -1
    loop_count = 0

    queens = []
    for r in range(0, N):
        c = min_threat_col(queens, r)
        queens.append(c)
        cols[c] += 1
        left_diagonal[c + r - 1] += 1
        right_diagonal[N - c + r] += 1

def threat_count(queens, row, col):
    count = cols[col] + left_diagonal[col + row - 1] + right_diagonal[N - col + row]
    return count

def min_threat_col(queens, row):
    min = 1001
    mark_cols = []
    for i in range(0, N):
        count = threat_count(queens, row, i)
        if count < min:
            min = count
            mark_cols = []
        if count == min:
            mark_cols.append(i)

    return mark_cols[random.randint(0, len(mark_cols) - 1)]

def most_threated_queen(queens, liq):
    threated_queens = []
    max = 1
    for r, c in enumerate(queens):
        count = threat_count(queens, r, c) - 3
        if count > max:
            max = count
            threated_queens = []
        if count == max:
            threated_queens.append(r)
    if len(threated_queens) == 0: return -1
    while True:
        q = threated_queens[random.randint(0, len(threated_queens) - 1)]
        if q == liq:
            if len(threated_queens) == 1:
                return -2
            else:
                continue
        else:
            return q

def print_board(queens):
    for c in queens:
        print c,
    print

start_time = time.time()
queens = []
last_iterative_queen = -1
loop_count = 0
restart_count = 0
left_diagonal = []
right_diagonal = []
cols = []
init()

while True:
    threated_queen = most_threated_queen(queens, last_iterative_queen)
    if threated_queen == -1:
        break
    elif threated_queen == -2:
        init()
        restart_count += 1
    else:
        last_iterative_queen = threated_queen
        curr_col = queens[threated_queen]
        cols[curr_col] -= 1
        left_diagonal[curr_col + threated_queen - 1] -= 1
        right_diagonal[N - curr_col + threated_queen] -= 1
        min_col = min_threat_col(queens, threated_queen)
        queens[threated_queen] = min_col
        cols[min_col] += 1
        left_diagonal[min_col + threated_queen - 1] += 1
        right_diagonal[N - min_col + threated_queen] += 1
        loop_count += 1
    if loop_count > 100:
        init()
        restart_count += 1

for r, c in enumerate(queens):
    print ("%d %d") % (r + 1, c + 1)
print "\n---- %d loop ----" % loop_count
print "---- %fs ----" % (time.time() - start_time)
print "Restart : %d times" % restart_count