import sys

n = int(sys.stdin.readline())

def sub(n):
    print(n)
    if n == 0:
        return 0
    elif n % 3 == 0:
        a = n // 3
        return sub(a)
    elif n % 2 == 0:
        a = n // 2
        return sub(a)
    else:
        return sub(n - 1)
        
print(sub(n))