import sys

n = int(sys.stdin.readline())
memo = [0 for _ in range(10000)]
memo[0] = 1
memo[1] = 1
pos = 1
data = []
    
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])

for i in range(n):
    if memo[data[i][0]] == 0:
        for j in range(pos + 1, data[i][0] + 1):
            memo[j] = memo[j - 2] + memo[j - 1]

        pos = data[i][0] - 1
        
    print(f"Case #{i + 1}: {memo[data[i][0] - 1] % data[i][1]}")