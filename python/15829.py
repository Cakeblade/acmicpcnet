import sys
import math

n = int(sys.stdin.readline())
char = [chr(i) for i in range(97, 123)]

string = str(sys.stdin.readline())
hashed = [0 for _ in range(n)]


def binary(data, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] < target:
        return binary(data, target, mid + 1, end)
    elif data[mid] > target:
        return binary(data, target, start, mid - 1)
    else:
        return mid

for i in range(n):
    hashed[i] = (binary(char, string[i], 0, 25) + 1)
    hashed[i] = hashed[i] * (31 ** i)
    
print(sum(hashed) % 1234567891)