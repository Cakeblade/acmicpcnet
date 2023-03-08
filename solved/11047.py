import sys

n, k = map(int, sys.stdin.readline().split())
worth = []

for i in range(n):
    worth.append(int(sys.stdin.readline()))
    
cnt = 0
index = n - 1

while k > 0:
    if k - worth[index] < 0:
        index -= 1
    else:
        i = k // worth[index]
        k = k - (i * worth[index])
        cnt += i
        
print(cnt)