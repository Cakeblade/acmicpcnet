import sys

n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start, end = 0, max(data)

while start <= end:
    mid = (start + end) // 2
    tree = 0
    for i in data:
        if i > mid:
            tree += i - mid
    
    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)