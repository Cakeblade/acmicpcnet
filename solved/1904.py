import sys

n = int(sys.stdin.readline())
memo = [0] * 1000001
memo[0], memo[1] = 1, 1

for j in range(2, n + 1):
    memo[j] = (memo[j - 2] + memo[j - 1]) % 15746

print(memo[n])