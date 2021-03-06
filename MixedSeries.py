"""Consider the below series:
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17, ...
This series is a mixture of 2 series - all the odd terms in this series form a Fibonacci series
and all the even terms are the prime numbers in ascending order.
Write a program to find the Nth term in this series.
The value N is a Positive integer that should be read from STDIN.
The Nth term that is calculated by the program should be written to STDOUT.
Other than the value of Nth term, no other characters/strings or message should be written to STDOUT.
For example, when N = 14, the 14th term in the series is 17.
So only the value 17 should be printed to STDOUT."""

def FindNextPrime(prev):
    prev += 1
    while True:
        for x in range(2, prev):
            if prev % x == 0:
                break
            elif x == prev-1:
                return(prev)
        prev += 1

def FindNextFib(p1,p2):
    return(p1+p2)


list = [1, 2, 1, 3]
N = int(input())
if N > 4:
    for i in range(4, N):
        # even = prime , odd = fibonacci
        if (i+1)%2 == 0:
            list.append(FindNextPrime(list[i-2]))
        else:
            list.append( FindNextFib(list[i-2],list[i-4]))



print(list[N-1])






