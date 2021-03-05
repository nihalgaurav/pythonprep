s = input().strip().rstrip()
count = 0
mx = 0
if s[0] == "0" and s[-1] == "0" and ("1" in s):
    i = -1
    while s[i] == "0":
        count += 1
        i -= 1

for x in range(len(s)):
    try:
        if s[x] == "0" and s[x-1] == "0":
            count += 1
        elif s[x] == "0":
            count = 1
        else:
            count = 0
    except:
        pass
    if mx < count:
        mx = count

print(mx)
