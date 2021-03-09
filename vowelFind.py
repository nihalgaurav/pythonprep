# first method : using for loop

# vowel = "AaEeIiOoUu"
# msg = "Hello Welcome"
# count = [each for each in msg if each in vowel]
# print(count)
# print(len(count))

# secound method : using dictinory

vowel = "aeiou"
msg = "vidhan rai"

msg = msg.casefold()
dict = {}.fromkeys(vowel, 0)
for ch in msg:
    if ch in dict:
        dict[ch] += 1
print(dict)