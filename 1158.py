import sys

n, k = map(int, sys.stdin.readline().split())
data = [i for i in range(1, n + 1)]
output = []
cur = 0

for i in range(n):
    cur += (k - 1)
    cur %= len(data)
    output.append(data.pop(cur))
    
print("<", end = "")
for i in range(n):
    print(f"{output[i]}", end = "")
    if i == n - 1:
        print(">")
    else:
        print(",", end = " ")