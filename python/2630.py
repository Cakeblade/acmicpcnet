import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []
w, b = 0, 0

def quad(x, y, n):
    global w, b
    c = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if c != data[i][j]:
                quad(x , y, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                return
    if c == 0:
        w += 1
    else:
        b += 1
        
quad(0, 0, n)
print(w)
print(b)