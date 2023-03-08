import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
sorted_data = sorted(set(data))

dic = {sorted_data[i] : i for i in range(len(sorted_data))}

for i in data:
    print(dic[i], end = ' ')