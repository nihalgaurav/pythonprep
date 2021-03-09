N = int(input())
for x in range(N):
    for y in range(N):
        # print("*  ", end="")
        if x == 0 or y == 0 or x == y or y == N-x-1 or x == N-1 or y == N-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("", end="\n")