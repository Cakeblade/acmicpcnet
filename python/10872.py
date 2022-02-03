import sys

inputl = sys.stdin.readline

def factorial(i):
	if i == 1:
		return 1
	elif i == 0:
		return 1
	return i * factorial(i-1)

a = int(inputl())
print(factorial(a))