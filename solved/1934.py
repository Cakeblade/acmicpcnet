import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    data.append([x, y])
    
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
        
    return a

for i in data:
    print(int((i[0] * i[1]) / (gcd(i[0], i[1]))))