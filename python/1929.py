import sys
import math

def check_pnum(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True
                   
n, m = map(int, sys.stdin.readline().split())
for i in range(n, m + 1):
    if check_pnum(i) == True:
        print(i)