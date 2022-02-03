import sys

inputl = sys.stdin.readline

while True:
	num1, num2 = map(int, inputl().split())
	if num1 == 0 and num2 == 0:
		break
	print(num1 + num2)