import sys

n = int(sys.stdin.readline())
data = []
zero = [1, 0, 1]
one = [0, 1, 1]

for i in range(n):
    data.append(int(sys.stdin.readline()))
    
def fibo(n):
    end = len(zero)
    if n >= end:
        for i in range(end, n + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[n], one[n])

    
for i in data:
    fibo(i)