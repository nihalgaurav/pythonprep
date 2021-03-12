# find the length of the longest substring without the repeatition of the letter
S = input()
length = []
for i in range(len(S)):
    sub = ""
    j = i
    # print(i)
    while j < len(S) and S[j] not in sub:
        sub = sub + S[j]
        j += 1
        # print(j)
    length.append(len(sub))
    # print(sub)
    sub = ""
print(max(length))