import sys

n = int(sys.stdin.readline())
m = 0
c = 0

while n > m:
    c += 1
    m += c

g = m - n
if c % 2 == 0:
    num = c - g
    deno = g + 1

else:
    num = g + 1
    deno = c - g

print(f"{num}/{deno}")