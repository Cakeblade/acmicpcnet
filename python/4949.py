import sys

data = []
output = []

while True:
    inp = sys.stdin.readline().rstrip()
    if inp == '.':
        break
    else:
        data.append(inp)
        
for i in data:
    stack = []
    flag = True
    for j in i:
        if j == '(' or j == '[':
            stack.append(j)
            
        elif stack and (j == ')' or j == ']'):
            if j == ')' and stack[-1] == '(':
                stack.pop()
                
            elif j == ']' and stack[-1] == '[':
                stack.pop()
                
            else:
                flag = False
        
        elif not stack and (j == ')' or j == ']'):
            flag = False
                    
    if flag and not stack:
        output.append("yes")
        
    else:
        output.append("no")
            
for i in output:
    print(i)