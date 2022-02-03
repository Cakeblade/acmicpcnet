import sys

inputl = sys.stdin.readline

size = int(inputl())
li = []
for i in range(size):
    li.append(int(inputl()))

for i in range(size):
    for j in range(size - 1):
        if li[j] > li[j + 1]:
            isdone = False
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

for i in range(size):
    print(li[i])