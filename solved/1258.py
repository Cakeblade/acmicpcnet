import sys

data = []

while True:
    i = int(sys.stdin.readline())
    if i == 0:
        break
    else:
        data.append(i)
        
for i in data:
    d = str(i)
    start = 0
    end = len(d) - 1
    mid = len(d) // 2
    flag = True
    while start != mid:
        if d[start] != d[end]:
            print("no")
            flag = False
            break
        else:
            start += 1
            end -= 1
    if flag == True:
        print("yes")
    