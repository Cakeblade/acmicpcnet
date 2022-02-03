import sys

data = []
memo = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if memo[a][b][c]:
        return memo[a][b][c]
    
    if a < b < c:
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

    else:
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return memo[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    
    else:
        data.append([a, b, c])

for i in range(len(data)):
    print(f"w({data[i][0]}, {data[i][1]}, {data[i][2]}) = {w(data[i][0], data[i][1], data[i][2])}")