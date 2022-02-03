import sys

inputl = sys.stdin.readline

t = int(inputl())
for i in range(t):
	num1, num2 = map(int, inputl().split())
	print(num1 + num2)