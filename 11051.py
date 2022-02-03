import sys
from math import factorial

n, k = map(int, input().split())
output = factorial(n) // (factorial(k) * factorial(n - k))
print(output % 10007)