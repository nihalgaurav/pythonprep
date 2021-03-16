number = 17
width = len(str(bin(number)[2:])) + 2
print("INT".rjust(width) + "OCT".rjust(width) + "HEX".rjust(width) + "BIN".rjust(width))
for x in range(1, number+1):
    print(str(int(x)).rjust(width, " ") + str(oct(x))[2:].rjust(width, " ") + str(hex(x))[2:].upper().rjust(width, " ")
          + str(bin(x)[2:]).rjust(width, " "))

num = 5
n = 97 + num
for i in range(num):
    p = ''
    for j in range(i):
        p = p + "-" + chr(n-i+j)
    print(p[::-1].rjust(num*2-2, "-") + chr(n-i-1) + p.ljust(num*2-2, "-"))

for i in range(num-2,-1, -1):
    p = ''
    for j in range(i):
        p = p + "-" + chr(n-i+j)
    print(p[::-1].rjust(num*2-2, "-") + chr(n-i-1) + p.ljust(num*2-2, "-"))