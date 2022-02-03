import sys

for line in sys.stdin:
	num1, num2 = map(int, line.split())
	print(num1 + num2)