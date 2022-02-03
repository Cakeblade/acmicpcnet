import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    data[i][0] = min(data[i - 1][1], data[i - 1][2]) + data[i][0]
    data[i][1] = min(data[i - 1][0], data[i - 1][2]) + data[i][1]
    data[i][2] = min(data[i - 1][0], data[i - 1][1]) + data[i][2]
    
print(min(data[n - 1]))