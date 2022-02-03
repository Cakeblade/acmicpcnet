import sys

n, m = map(int, sys.stdin.readline().split())
board = [str(sys.stdin.readline()) for _ in range(n)]
check = []

for i in range(0, n - 7):
    for x in range(0, m - 7):
        w = 0
        b = 0
        for j in range(i, i + 8):
            for y in range(x, x + 8):
                if (j + y) % 2 == 0:
                    if board[j][y] != 'W':
                        w += 1
                    if board[j][y] != 'B':
                        b += 1
                else:
                    if board[j][y] != 'B':
                        w += 1
                    if board[j][y] != 'W':
                        b += 1
        check.append(w)
        check.append(b)

print(min(check))