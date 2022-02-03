import sys

inputl = sys.stdin.readline

def solve(a: list) -> int:
	return sum(a)

if __name__ == '__main__':
	line = list(map(int, inputl().split()))
	print(solve(line))
