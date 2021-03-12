n = int(input())
p = abs(n)
r = 0
while p >= 1:
    r = (r * 10) + (p % 10)
    p //= 10

if n < 0:
    print(-r)
else:
    print(r)