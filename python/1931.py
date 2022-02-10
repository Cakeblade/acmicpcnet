import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])

data = sorted(data, key = lambda x : x[0])
data = sorted(data, key = lambda x : x[1])
cnt = 0
a = 0

for i, j in data:
    if i >= a:
        cnt += 1
        a = j
    
print(cnt)