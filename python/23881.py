import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
num = [-1, -1]

for i in range(len(arr) - 1):
    _min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[_min]:
            _min = j
            cnt += 1
            if cnt == k:
                num = [arr[_min], arr[j]]
    arr[i], arr[_min] = arr[_min], arr[i]

if num[0] == -1 and num[1] == -1:
    print(num[0])
else:
    print(num[0], num[1])