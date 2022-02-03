import sys

n = int(sys.stdin.readline())
stack = [-1]

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        if stack[0] == -1:
            stack[0] = command[1]
            
        else:
            stack.insert(0, command[1])
    
    elif command[0] == "pop":
        if stack[0] == -1:
            print('-1')
            
        else:
            print(stack[0])
            if len(stack) == 1:
                stack[0] = -1
                
            else:
                stack.remove(stack[0])
            
    elif command[0] == "size":
        if stack[0] == -1:
            print('0')
            
        else:
            print(len(stack))
            
    elif command[0] == "empty":
        if stack[0] == -1:
            print('1')
            
        else:
            print('0')
    elif command[0] == "top":
        if stack[0] == -1:
            print('-1')
            
        else:
            print(stack[0])
            
            
