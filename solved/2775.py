import sys

t = int(sys.stdin.readline())
output = []

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    apart = [i for i in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            apart[j] += apart[j - 1]
    output.append(apart[-1])
    
for i in output:
    print(i)