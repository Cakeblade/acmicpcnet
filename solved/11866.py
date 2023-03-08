import sys

n, k = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]
output = []
index = 0

for i in range(n):
    for j in range(k - 1):
        if (index + 1) >= len(data):
            index = 0
        else:
            index += 1
            
    output.append(data[index])
    del data[index]
    if index == len(data):
        index = 0
    
print("<", end = '')
for i in range(n):
    print(output[i], end = '')
    if i != n - 1:
        print(', ', end = '')
print(">", end = '')