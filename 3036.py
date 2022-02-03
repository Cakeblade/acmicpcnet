import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

def gcd(x, y):
    while y != 0:
        n = x % y
        x = y
        y = n
    return x

for i in range(1, n):
    a = gcd(data[0], data[i])
    print(f"{data[0] // a}/{data[i] // a}")