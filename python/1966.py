import sys

n = int(sys.stdin.readline())
output = []

for i in range(n):
    x, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    index = [0 for i in range(x)]
    index[m] = 1
    cnt = 0
    while True:
        if data[0] == max(data):
            cnt += 1
            if index[0] == 1:
                output.append(cnt)
                break
            else:
                del data[0]
                del index[0]
        else:
            data.append(data[0])
            del data[0]
            index.append(index[0])
            del index[0]
            
for i in output:
    print(i)