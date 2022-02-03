import sys
"""
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def binary(l, a, start, end):
    if start > end:
        return 0
    i = (start + end) // 2
    if l == a[i]:
        return 1
    elif l < a[i]:
        return binary(l, a, start, i - 1)
    else:
        return binary(l, a, i + 1, end)
        
for l in b:
    start = 0
    end = n - 1
    print(binary(l, a, start, end))
"""
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

for l in b:
    sys.stdout.write('1\n') if l in a else sys.stdout.write('0\n')