import sys

n = int(sys.stdin.readline())
memo = [0, 1, 2, 3, 2]

for i in range(n):
    j, min = 1, 2500000001
    while j * j < i:
        tmp = i - j * j
        if min > tmp:
            min = memo[tmp]

        j += 1
    
    memo.append(min + 1)

print(memo[n])