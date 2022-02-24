import sys

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max = -1
output = -1
for i in range(n):
    result = set()
    for j in range(5):
        for k in range(n):
            if data[i][j] == data[k][j]:
                result.add(k)               
    
    if len(result) > max:
        output = i + 1
        max = len(result)
        
print(output)