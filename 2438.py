import sys

inputl = sys.stdin.readline

n = int(inputl())

for i in range(n):
	for j in range(i + 1):
		print('*', end='')
	print()