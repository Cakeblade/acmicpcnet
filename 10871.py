import sys

inputl = sys.stdin.readline

n, x = map(int, inputl().split())
line = list(map(int, inputl().split()))

for i in range(n):
	if x > line[i]:
		print(line[i], end=' ')