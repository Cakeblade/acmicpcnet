import sys
import math

n, k = map(int, sys.stdin.readline().split())

nk = math.factorial(k) * math.factorial(n - k)
print(int(math.factorial(n) / nk))