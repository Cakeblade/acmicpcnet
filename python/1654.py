import sys

k, n = map(int, sys.stdin.readline().split())
data = []
output = 0

for i in range(k):
    data.append(int(sys.stdin.readline()))
    
data.sort()
    
def binary(data, low, high):
    while low <= high:
        mid = (low + high) // 2
        num = 0
        for l in data: 
            num += (l // mid)

        if num >= n:
            low = mid + 1 
        else:
            high = mid - 1
    
    return high

print(binary(data, 1, max(data) + 1))