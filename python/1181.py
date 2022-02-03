import sys

n = int(sys.stdin.readline())
data = []

for i in range(n):
    data.append(sys.stdin.readline().strip())
    
setdata = set(data)
data = list(setdata)
data.sort()
data.sort(key = len)

for i in range(len(data)):
    print(data[i])