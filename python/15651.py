import sys

n, m = map(int, sys.stdin.readline().split())
data = []

def back():
    if len(data) == m:
        print(' '.join(map(str, data)))
        return
    
    for i in range(1, n + 1):
        data.append(i)
        back()
        data.pop()
        
back()