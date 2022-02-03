import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(str(sys.stdin.readline()))
    
for i in range(n):
    flag = 0
    for j in data[i]:
        if j == '(':
            flag += 1
        elif j == ')':
            flag -= 1
        if flag < 0:
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")