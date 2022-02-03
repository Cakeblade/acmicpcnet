import sys

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
memo = [0 for _ in range(101)]
memo[0], memo[1], memo[2], memo[3], memo[4] = 1, 1, 1, 2, 2

def p(x):
    if x <= 4:
        return memo[x]
    
    if memo[x] != 0:
        return memo[x]
    
    memo[x] = p(x - 1) + p(x - 5)
    return memo[x]

for i in data:
    print(p(i - 1))