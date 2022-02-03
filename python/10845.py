import sys

n = int(sys.stdin.readline())
queue = [-1]

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        if queue[0] == -1:
            queue[0] = command[1]
            
        else:
            queue.insert(0, command[1])
            
    elif command[0] == "pop":
        if queue[0] == -1:
            print("-1")
            
        else:
            print(queue[len(queue) - 1])
            if len(queue) == 1:
                queue[0] = -1
                
            else:
                queue.pop()
            
    elif command[0] == "size":
        if queue[0] == -1:
            print("0")
            
        else:
            print(len(queue))
            
    elif command[0] == "empty":
        if queue[0] == -1:
            print("1")
            
        else:
            print("0")
            
    elif command[0] == "front":
        print(queue[len(queue) - 1])
        
    elif command[0] == "back":
        print(queue[0])
        
    else:
        print("Error!")
            
