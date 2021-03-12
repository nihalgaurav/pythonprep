N = int(input())
for i in range(0, N):
    print(("*"*(2*i+1)).ljust(2*N, " "))

for i in range(0, N):
    print(("*"*(2*i+1)).rjust(2*N, " "))

for i in range(0, N):
    print(("*"*(2*i+1)).center(2*N, " "))

for i in range(0,N//2 +1):
    print(("*"*(2*i+1)).center(N, " "))


n = N

for i in range(n):
    print(("*"*(2*i+1)).center(2*n-1, " "))
for i in range(n):
    i = n-i-1
    print(("*"*(i+1)).rjust(n, " "))
for i in range(n):
    print(("*"*(i+1)).rjust(n, " "))
for i in range(n):
    i = n-i -1
    print(("*"*(2*i+1)).center(2*n-1, " "))
