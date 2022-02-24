import sys

n, m = map(str, sys.stdin.readline().split())

n = int(n, 2)
m = int(m, 2)

print(bin(n + m)[2:])