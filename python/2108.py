import sys
from collections import Counter

def mode(a):
    c = Counter(a)
    o = c.most_common()
    maximum = o[0][1]
    
    modes = []
    for i in o:
        if i[1] == maximum:
            modes.append(i[0])
            
    return modes

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()
modes = mode(a)
modes.sort()

print(f'{(sum(a) / n):.0f}')
print(a[len(a) // 2])
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])
print(max(a) - min(a))