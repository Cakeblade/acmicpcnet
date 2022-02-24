import sys

n = int(sys.stdin.readline())
data = [0] + list(map(int, sys.stdin.readline().split()))
memo = [0] * (n + 1)
memo[1] = data[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        memo[i] = max(memo[i], memo[i - j] + data[j])

print(memo[n])