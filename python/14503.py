import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def clean(r, c, d):
    global cnt
    if data[r][c] == 0: #cleaning
        data[r][c] = 2
        cnt += 1
    
    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + dx[nd]
        nc = c + dy[nd]
        if data[nr][nc] == 0:
            clean(nr, nc, nd)
            return
        d = nd
    
    nd = (d + 2) % 4
    nr = r + dx[nd]
    nc = c + dy[nd]
    if data[nr][nc] == 1:
        return
    
    clean(nr, nc, d)

    
cnt = 0
clean(r, c, d)
print(cnt)