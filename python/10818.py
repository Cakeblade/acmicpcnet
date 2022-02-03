import sys

inputl = sys.stdin.readline

n = int(inputl())
line = list(map(int, inputl().split()))
maxx = max(line)
minn = min(line)
print(minn, maxx)