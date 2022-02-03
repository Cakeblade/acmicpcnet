import sys

def mul_ma(a, am, bm):
    re = [[0 for i in range(a)] for j in range(a)]
    for i in range(a):
        for j in range(a):
            for l in range(a):
                re[i][j] += (am[i][l] * bm[l][j]) % 1000
    
    return re
 
def devide(a, b, ma):
    if b == 1:
        return ma
    
    elif b == 2:
        return mul_ma(a, ma, ma)
    
    else:
        temp = devide(a, b // 2, ma)
        
        if b % 2 == 0:
            return mul_ma(a, temp, temp)
        
        else:
            return mul_ma(a, mul_ma(a, temp, temp), ma)

a, b = map(int, sys.stdin.readline().split())
ma = [list(map(int, sys.stdin.readline().split())) for _ in range(a)]
 
for i in devide(a, b, ma):
    for j in i:
        print(j % 1000, end = ' ')
        
    print()