import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in data:
    avg = (sum(i) - i[0]) / i[0]
    cnt = 0
    for j in range(1, i[0] + 1):
        if i[j] > avg:
            cnt += 1
    
    print(f"{(cnt / i[0]) * 100:.3f}%")