import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
data = [list(map(int, input())) for _ in range(n)]
result = []

def quad(x, y, n):
    c = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if c != data[i][j]:
                print("(", end = '')
                quad(x , y, n // 2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                print(")", end = '')
                return
    
    if c == 1:
        print(1, end = '')
    
    else:
        print(0, end = '')
    
quad(0, 0, n)