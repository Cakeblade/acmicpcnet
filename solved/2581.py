import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

pnum = [-1]

def is_pnum(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        
    return True

for i in range(m, n + 1):
    a = 0
    if is_pnum(i) and i > 1:
        if pnum[0] == -1:
            pnum[0] = i
        else:
            pnum.append(i)
    
if pnum[0] == -1:
    print(-1)
    
else:
    print(sum(pnum))
    print(pnum[0])
    