import sys

n, m = map(int, sys.stdin.readline().split())
site = {}
index = []

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    site[a] = b

for i in range(m):
    c = sys.stdin.readline().rstrip()
    index.append(c)

for key in index:
    print(site[key])