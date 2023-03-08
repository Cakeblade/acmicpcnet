import sys

n = int(sys.stdin.readline())
data = []
rank = []

for i in range(n):
    w, h = map(int, sys.stdin.readline().split())
    data.append([w, h])
    
for i in range(n):
    cnt = 0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    rank.append(cnt + 1)

print(*rank)