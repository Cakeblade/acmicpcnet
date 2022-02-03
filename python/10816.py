import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
a = [0 for _ in range(m)]

dic = dict()

for i in cards:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in range(m):
    if h[i] in dic:
        print(dic[h[i]], end = ' ')
    else:
        print('0', end = ' ')
