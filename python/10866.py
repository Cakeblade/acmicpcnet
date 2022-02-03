import sys

n = int(sys.stdin.readline())
deck = [-1]

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push_front":
        if deck[0] == -1:
            deck[0] = command[1]
            
        else:
            deck.insert(0, command[1])
            
    elif command[0] == "push_back":
        if deck[0] == -1:
            deck[0] = command[1]
            
        else:
            deck.append(command[1])
            
    elif command[0] == "pop_front":
        if deck[0] == -1:
            print("-1")
            
        else:
            print(deck[0])
            if len(deck) == 1:
                deck[0] = -1
                
            else:
                deck.remove(deck[0])
                
    elif command[0] == "pop_back":
        if deck[0] == -1:
            print("-1")
            
        else:
            print(deck[len(deck) - 1])
            if len(deck) == 1:
                deck[0] = -1
                
            else:
                deck.pop()
            
    elif command[0] == "size":
        if deck[0] == -1:
            print("0")
            
        else:
            print(len(deck))
            
    elif command[0] == "empty":
        if deck[0] == -1:
            print("1")
            
        else:
            print("0")
            
    elif command[0] == "front":
        print(deck[0])
        
    elif command[0] == "back":
        print(deck[len(deck) - 1])
        
    else:
        print("Error!")
            
