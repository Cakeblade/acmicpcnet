import sys
import math

n = int(sys.stdin.readline())
data = []

def combi(n, r):
    return int(math.factorial(n) / (math.factorial(n - r) * math.factorial(r)))
        
for i in range(0, n):    
    a, b = map(int, sys.stdin.readline().split())
    data.append([a, b])

for i in range(0, n):
    print(combi(data[i][1], data[i][0]))