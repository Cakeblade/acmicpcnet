import sys

data = []

while True:
    x, y, z = map(int, sys.stdin.readline().split())
    if x == 0 and y == 0 and z == 0:
        break
    else:
        data.append([x, y, z])

for i in data:
    i.sort()
    if (i[2] ** 2) == ((i[0] ** 2) + (i[1] ** 2)):
        print("right")
    else:
        print("wrong")