import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

for i in range(m):
    for j in range(n):
        if data[i][j] == 1:
            q.append([i, j])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < m and 0 <= ny < n and data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            q.append([nx, ny])


for i in data:
    for j in i:
        if j == 0:
            print(-1)
            exit()

    cnt = max(cnt, max(i))

print(cnt - 1)