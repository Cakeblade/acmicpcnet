import sys
inputl = sys.stdin.readline

def star():
	for i in range(0,3):
		for j in range(0,3):
			if j == 1 & i == 1:
				print(' ', end='')
			else:
				a()
		print()
def a():
	for i in range(0,3):
		for j in range(0,3):
			if j == 1 & i == 1:
				print(' ', end='')
			else:
				print('*', end='')
		print()

star()