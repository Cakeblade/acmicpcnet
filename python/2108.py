import sys
from collections import Counter

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
data.sort()

cnt = Counter(data).most_common(2)

print(round(sum(data) / n))
print(data[n // 2])
if n > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    
    else:
        print(cnt[0][0])

else:
    print(cnt[0][0])

print(max(data) - min(data))