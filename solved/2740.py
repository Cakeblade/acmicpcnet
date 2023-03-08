import sys

n, m = map(int, sys.stdin.readline().split())
am = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

m, k = map(int, sys.stdin.readline().split())
bm = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

ma = [[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            ma[i][j] += am[i][l] * bm[l][j]
        
for i in ma:
    print(*i)
    
    