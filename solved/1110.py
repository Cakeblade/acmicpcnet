import sys

inputl = sys.stdin.readline

n = int(inputl())
firN = n
cnt = 1
a = (int(n / 10) + (n % 10)) % 10
n = (n % 10) * 10 + a
while n != firN:
	a = (int(n / 10) + (n % 10)) % 10
	n = (n % 10) * 10 + a
	cnt += 1
print(cnt)