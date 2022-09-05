import sys

n, m = map(int, sys.stdin.readline().split())

listen = set()
see = set()

for i in range(n):
    data = sys.stdin.readline()
    data = data[:-1]
    listen.add(data)

for i in range(m):
    data = sys.stdin.readline()
    data = data[:-1]
    see.add(data)

output = list(listen & see)
output.sort()

print(len(output))
for out in output:
    print(out)