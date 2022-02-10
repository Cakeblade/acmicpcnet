import sys

n = int(sys.stdin.readline())
cnt = 1
while cnt * (cnt + 1) / 2 <= n:
    cnt += 1

print(cnt - 1)