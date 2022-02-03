import sys

n, m = map(int, sys.stdin.readline().split())
data = [True for _ in range(n + 1)]
cnt = 0

for i in range(2, len(data) + 1):
    for j in range(i, n + 1, i):
        if data[j] == True:
            data[j] = False
            cnt = cnt + 1
            
            if cnt == m:
                print(j)
                break