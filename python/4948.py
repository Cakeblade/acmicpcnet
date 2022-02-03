import sys
import math
sys.stdin = open("input.txt", "r")
a = []
data = []

def chk(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
        
    return True

for i in range(2, 246912):
    if chk(i):
        a.append(i)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    else:
        cnt = 0
        for i in a:
            if n < i <= (2 * n):
                cnt += 1
        data.append(cnt)
        
for i in data:
    print(i)