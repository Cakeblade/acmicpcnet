import sys

memo = [0 for i in range(46)]

def fibo(n):
    if n <= 1:
        return n
    if memo[n] != 0:
        return memo[n]
    memo[n] = (fibo(n - 2) + fibo(n - 1))
    return memo[n]

n = int(sys.stdin.readline())

print(fibo(n))