import sys

n = int(sys.stdin.readline())
satan = 666

while n != 0:
    if "666" in str(satan):
        n -= 1
        if n == 0:
            break
    satan += 1
    
print(satan)