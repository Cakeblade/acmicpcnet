import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]
data = deque(data)
output = []

while data:
    for i in range(k - 1):
        data.append(data.popleft())
    
    output.append(data.popleft())
    
print("<", end = '')
for i in range(n):
    print(output[i], end = '')
    if i != n - 1:
        print(', ', end = '')
print(">", end = '')