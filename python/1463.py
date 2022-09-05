import sys

n = int(sys.stdin.readline())
data = [0, 0, 1, 1]

for i in range(4, n + 1):
    data.append(data[i - 1] + 1)
    if i % 3 == 0:
        data[i] = min(data[int(i / 3)] + 1, data[i])
    if i % 2 == 0:
        data[i] = min(data[int(i / 2)] + 1, data[i])

print(data[n])