import sys

n = int(sys.stdin.readline())
case = []

for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    case.append([x, y, z])
    
for i in range(n):
    w = case[i][2] // case[i][0] + 1
    f = case[i][2] % case[i][0]
    if case[i][2] % case[i][0] == 0:
        w = case[i][2] // case[i][0]
        f = case[i][0]
        
    print(f * 100 + w)