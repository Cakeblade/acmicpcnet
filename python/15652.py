import sys

n, m = map(int, sys.stdin.readline().split())
data = []

def back(a):
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    
    for i in range(a, n + 1):
        data.append(i)
        back(i)
        data.pop()

back(1)