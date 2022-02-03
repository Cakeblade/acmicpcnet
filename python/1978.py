import sys
import math

def is_pnum(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in data:
    if is_pnum(i) == True:
        cnt += 1

print(cnt)