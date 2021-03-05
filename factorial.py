"""this programe finds factorial of a given number"""

N = int(input())
fact = [1]
for i in range(2, N+1):
    if N % i == 0:
        fact.append(i)

print(*fact, sep=", ")

