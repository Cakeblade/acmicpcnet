import sys

n, c = map(int, sys.stdin.readline().split())
pos = [int(sys.stdin.readline()) for _ in range(n)]
pos.sort()

left = 1
right = pos[-1] - pos[0]
ans = 0


while left <= right:
    mid = (left + right) // 2
    d = pos[0]
    cnt = 1

    for i in range(1, len(pos)):
        if pos[i] >= d + mid:
            cnt += 1
            d = pos[i]

    if cnt >= c:
        left = mid + 1
        ans = mid

    else:
        right = mid - 1

print(ans)