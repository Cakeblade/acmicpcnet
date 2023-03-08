import sys

data = sys.stdin.readline()
a = sorted(data, reverse = True)

for i in a:
    print(i, end = '')