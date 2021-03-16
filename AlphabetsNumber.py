s = "abcdefghijklmnopqrstuvwxyz"

for x in s:
    print(x.upper().ljust(3) + str(ord(x.upper())).ljust(5) + x.rjust(3) + str(ord(x)).rjust(5))