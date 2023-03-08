import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

stack = []
output = []

flag = 0
cur = 1

for i in range(n):
    m = int(sys.stdin.readline())
    
    while cur <= m:
        stack.append(cur)
        output.append("+")
        cur += 1
        
    if stack[-1] == m:
        stack.pop()
        output.append("-")
    
    else:
        print("NO")
        flag = 1
        break
        
if flag == 0:
    for i in output:
        print(i)