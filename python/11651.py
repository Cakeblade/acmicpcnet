import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])
    
data.sort(key = lambda x : [x[1], x[0]])

for i in data:
    print(f"{i[0]} {i[1]}")