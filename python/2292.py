import sys

n = int(sys.stdin.readline())

beehouse = 1
cnt = 1

while n > beehouse:
    beehouse += (cnt * 6)
    cnt += 1

print(cnt)