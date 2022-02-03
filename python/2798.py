import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))
com = list(combinations(data, 3))

a = -1
index = -1

for i in range(len(com)):
    b = sum(com[i])
    if b < m:
        if b > a:
            a = b
            index = i
        
    elif sum(com[i]) == m:
        index = i
        break
        
print(sum(com[index]))