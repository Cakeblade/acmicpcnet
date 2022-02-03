import sys
import math

def check(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        
    return True
    
n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(int(sys.stdin.readline()))

for i in data:
    a = i // 2
    b = i // 2

    for j in range(i // 2):
        if check(a) and check(b):
            print(a, b)
            break
        else:
            a = a - 1
            b = b + 1
        