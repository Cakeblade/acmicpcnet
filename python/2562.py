import sys

inputl = sys.stdin.readline

line = list()
max_V = -1
for i in range(0, 9):
	line.append(int(inputl()))
	if line[i] > max_V:
		max_V = line[i]
		max_I = i + 1
print(max_V)
print(max_I)