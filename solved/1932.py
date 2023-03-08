import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
deep = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            data[i][j] += data[i - 1][j]
            
        elif j == i:
            data[i][j] += data[i - 1][j - 1]
            
        else:
            data[i][j] += max(data[i - 1][j], data[i - 1][j - 1])
            
print(max(data[-1]))