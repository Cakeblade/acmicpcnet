import sys

n = int(sys.stdin.readline())
cnt = 2

while n > 0:
    if n % cnt == 0:
        n = n // cnt
        print(cnt)
    else:
        cnt += 1
