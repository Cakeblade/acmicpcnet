import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
m = 0

data.sort()

for i in range(n):
    for j in range(i + 1):
        m += data[j]
        
print(m)