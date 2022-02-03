import sys

n, m, b = map(int, sys.stdin.readline().split())
matrix = []
height = [0 for _ in range(257)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        height[t[j]] += 1
    matrix.append(t)
    
ma = 100000000000000
mi = 0
    
for i in range(257):
    x = 0
    y = 0
    for j in range(257):
        if i > j:
            x += (i - j) * height[j]
        
        else:
            y += (j - i) * height[j]
    
    inven = b + y - x
    if inven < 0:
        continue
    
    z = y * 2 + x
    if z <= ma:
        ma = z
        mi = i
    
print(ma, mi)