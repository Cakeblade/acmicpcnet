import sys

n, m = map(int, sys.stdin.readline().split())
ans = 0
price = []

for _ in range(m):
    price.append(list(map(int, sys.stdin.readline().split())))

pack = sorted(price, key = lambda x : x[0])[0][0]
single = sorted(price, key = lambda x : x[1])[0][1]

if pack <= single * 6:
    ans = pack * (n // 6) + single * (n % 6)
    if pack < single * (n % 6):
        ans = pack * ((n // 6) + 1)
else:
    ans = single * n

print(ans)